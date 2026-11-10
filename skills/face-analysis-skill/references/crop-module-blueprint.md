# Blueprint — professional face detect / align / crop module

A reusable design for a **local, high-precision face detection + alignment + cropping** module.
Use this when the user wants a real tool (not just "find faces"): configurable crop styles,
adaptive margins, aspect-ratio preservation, transparent backgrounds, batch processing, QA of
bad crops, and GPU-optional local inference.

> This is a **blueprint the skill follows when building**, not a vendored app. Inspect any
> existing project first, match its architecture, and never overwrite files without reading them.

## Hard rules (do / don't)

- **Never deform the face** — no non-uniform scaling, no squashing to force an output ratio.
  Letterbox/pad to hit a target ratio, don't stretch.
- **Never crop from a fixed rectangle alone.** Drive the crop from detection + landmarks (+
  segmentation for hair/ears), with adaptive margins.
- **Preserve the original aspect ratio** of facial geometry; only the *canvas* ratio is configurable.
- Handle **image borders, coordinates and padding** explicitly — clamp, or pad the source
  (reflect/replicate/transparent) when the desired crop runs past the edge, so you never read OOB.
- **Don't claim precision you didn't measure.** Report measured numbers; mark a crop low-confidence
  instead of asserting it's perfect.
- **Verify licenses & version compatibility** of both code *and* weights before shipping.

## Module layout (keep stages independent)

```
face_crop/
  io/            load images (Pillow/OpenCV), list batches, write outputs
  detection/     faces -> boxes + score + 5pt  (InsightFace SCRFD; OpenCV YuNet fallback)
  selection/     pick primary face; allow choosing another (index / click / largest / most-central)
  landmarks/     5/68/468 pts; eyes, nose, mouth, contour; head-pose/roll estimate
  alignment/     similarity transform (eyes level), no shear/scale distortion
  segmentation/  face-parsing (BiSeNet) masks -> hair/ears/neck; alpha for transparent bg
  crop/          crop strategies + adaptive margins + aspect-ratio canvas + padding
  validation/    reject incomplete/low-confidence/out-of-frame crops
  export/        organized filenames, metadata sidecar, optional preview overlay
  pipeline.py    wires stages; config-driven (YAML/CLI)
```

Each stage takes explicit inputs/outputs (numpy image + dataclasses), so stages are unit-testable
in isolation and swappable (e.g. switch detector without touching crop logic).

## Primary-face selection (req. 2)

Default primary = highest `score * area * centrality` (configurable weights). Expose an override:
pick by index, by nearest to a click point, largest, or most-central. Return *all* faces ranked
so the UI/preview can offer alternatives.

## Alignment (req. 4)

1. Get eye centers (from 5-pt or landmark mean per eye).
2. Compute roll = angle between eyes; build a **similarity** transform (rotation + uniform scale +
   translation) — never an affine with shear.
3. Warp with `cv2.warpAffine` using `INTER_CUBIC`, border mode that matches your bg choice.
4. Keep the transform matrix so you can map landmarks/masks into the aligned frame too.

## Crop strategies (req. 5–7)

Compute margins as **multiples of interocular distance (IOD)** or face-box size, so they scale
with resolution. Clamp/pad at borders. All ratios are canvas-only (pad, don't stretch).

| Strategy | Includes | Typical framing (from landmarks) | Notes |
|---|---|---|---|
| `headshot` / primer plano | face, chin→forehead | ~1.4–1.8× face box, centered on nose | tightest; risk of cutting forehead/chin → use margins |
| `full_face` | hair + ears + chin | expand to **segmentation** hair/ear mask bounds + margin | needs face-parsing for correct hair/ear extent |
| `head_shoulders` | head + shoulders | extend downward ~1.5–2× face height, widen for shoulders | shoulders aren't in landmarks → use fixed ratio below chin |

**Adaptive margins (req. 6):** never use a flat pixel pad. Derive top/bottom/side margins from
IOD and, for `full_face`, from the parsing mask so hair/ears/chin/forehead aren't clipped. Grow
margins when head pose/roll is large.

**Transparent background (req. 7):** when `full_face`/`head_shoulders` + segmentation is on,
composite the person mask (face-parsing classes, or SAM2 for whole-person) to RGBA; otherwise
keep the original background and say so (don't fake alpha).

## Validation / QA (req. 10)

Flag a crop as **defective / low-confidence** (don't silently emit) when any:
- detector score < threshold, or face box area below a min fraction of the image;
- a required landmark/region falls outside the crop (forehead/chin/ear clipped) per the mask;
- head roll/yaw beyond limits after alignment;
- large occlusion (low visible-skin ratio from parsing) or extreme under/over-exposure;
- target region padded more than X% (crop ran off the source).
Emit a per-image status (`ok` / `review` / `rejected`) with reasons into the metadata sidecar.

## Difficult cases (req. 8)

Small faces → upscale ROI before landmarking; tilted → rely on alignment; partial/occluded →
SCRFD handles better than Haar; harsh light → CLAHE / gamma in preprocessing (don't bake it into
the saved crop unless asked). Keep a configurable detector `det_size` and score threshold.

## Preview (req. 9)

Render an overlay: detection rectangle(s) + chosen-face highlight, landmarks, the crop box for
the active strategy, and the final result thumbnail — as an image (and/or a small HTML/Matplotlib
preview). Preview is a *view*, separate from the export path.

## Batch & export (req. 11)

Walk a folder; process with a progress bar; write to a mirrored output tree. Filenames:
`{stem}__{strategy}__{faceIdx}.{png|jpg}` (PNG when alpha). Write a `.json` sidecar per image
(boxes, chosen index, transform, margins, validation status, timings). Resume-safe: skip existing
unless `--overwrite`.

## Recommended stack for the stated target (Windows + RTX 2060 6 GB)

Prioritize **lightweight** models; 6 GB VRAM rules out the heaviest segmenters.

- **Detection + landmarks:** InsightFace **`buffalo_s`** (SCRFD-500M + small recognition) via
  **ONNX Runtime**. Light, accurate, 5-pt landmarks. Fallback detector: **OpenCV YuNet**
  (`cv2.FaceDetectorYN`) — tiny, CPU-friendly.
- **Dense/real-time landmarks (optional):** **MediaPipe** Face Landmarker (468 + head pose),
  runs on CPU — good for preview and pose, frees VRAM.
- **Segmentation (hair/ears/alpha):** **face-parsing** (BiSeNet) exported to **ONNX** — far
  lighter than SAM2. Only reach for **SAM2** if you need whole-person/promptable masks, and then
  use a small checkpoint; `sam2-hiera-large` is heavy for 6 GB.
- **Runtime:** **ONNX Runtime** with `CUDAExecutionProvider` and a **`CPUExecutionProvider`
  fallback**; try FP16 for the detector. Keep sessions warm; batch where possible.
- **Image I/O / processing:** OpenCV (BGR, warps) + Pillow (RGBA export). Augmentation for any
  eval set with Albumentations (keypoint/mask-aware).

VRAM tips: run detection and segmentation as separate ORT sessions you can release; prefer
`det_size=(640,640)` or smaller; avoid loading SAM2-large and InsightFace simultaneously.

## Pinned dependencies — known-working baseline (verify before trusting)

Pin exact versions in `requirements.txt` and re-test; these are a starting point, not a guarantee.
On the RTX 2060 (CUDA), install the GPU ORT and a CUDA-matched PyTorch only if you use torch models.

```
# requirements.txt (CPU-safe baseline; swap onnxruntime -> onnxruntime-gpu on the 2060)
numpy==1.26.4
opencv-python==4.10.0.84
pillow==10.4.0
onnxruntime==1.18.1          # GPU: onnxruntime-gpu==1.18.1 (needs matching CUDA/cuDNN)
insightface==0.7.3
mediapipe==0.10.14
scikit-image==0.24.0
albumentations==1.4.15
pyyaml==6.0.2
tqdm==4.66.5
pytest==8.3.3
# face-parsing: install from the repo (no stable PyPI pin) and export to ONNX
# torch only if needed: install the CUDA build from pytorch.org, don't `pip install torch` blind
```

> ONNX Runtime GPU ↔ CUDA/cuDNN versions are strict — confirm the matrix for the ORT version you
> pin against the RTX 2060's driver before assuming GPU works; the CPU provider must still run.

## Tests & evaluation (req: unit tests + eval set + metrics)

- **Unit tests** per stage: coordinate/padding math at image borders, aspect-ratio canvas (no
  stretch), alignment angle, margin computation, filename/sidecar format, validation thresholds.
  Use tiny synthetic fixtures (drawn faces / known landmarks) so tests are deterministic & offline.
- **Eval set:** a labeled folder covering multi-face, tilted, small, occluded, backlit, varied
  resolutions. Store expected primary-face index and acceptable crop bounds.
- **Metrics to measure (don't fabricate):** detection rate, correct-primary rate, **% correct
  crops** (region-containment check, not eyeballing), per-stage latency (ms), end-to-end FPS, and
  peak **VRAM** (`torch.cuda.max_memory_allocated` or `nvidia-smi`). Report measured values with the
  test set and hardware; never assert a crop is perfect without the containment check passing.

## Run commands (shape the CLI like this)

```bash
python -m face_crop.pipeline --input ./in --output ./out --strategy full_face --ratio 4:5 --gpu
python -m face_crop.pipeline --input photo.jpg --strategy headshot --face-index 1 --preview
pytest -q
python -m face_crop.eval --set ./eval --report report.json   # prints measured metrics
```

Expose `--strategy {headshot,full_face,head_shoulders}`, `--ratio`, `--margin-scale`,
`--transparent`, `--min-score`, `--gpu/--cpu`, `--face-index`, `--overwrite`, `--preview`.
Document each strategy's **advantages and limits** (e.g. headshot is tightest but most likely to
clip forehead/chin on tilted faces; full_face needs good hair/ear segmentation; head_shoulders
uses a heuristic below the chin since shoulders aren't landmarked).
