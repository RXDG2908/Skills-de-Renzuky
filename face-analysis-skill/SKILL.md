---
name: face-detection-analysis
description: Pipeline guide for face detection and analysis in Python — pick the right library for each stage (detection, alignment/landmarks, parsing/segmentation, image preprocessing, local/accelerated inference) and wire them together, plus a full blueprint for building a professional local face detect/align/crop module (configurable crop styles, adaptive margins, aspect-ratio preservation, transparent backgrounds, batch, QA, tests/metrics). Covers InsightFace, RetinaFace, MediaPipe, OpenCV, Ultralytics YOLO, DeepFace, face_recognition, dlib, face-alignment, SAM2, face-parsing, Pillow, scikit-image, Albumentations, ONNX Runtime, PyTorch, OpenVINO, TensorRT. Use when the user wants to detect faces, extract facial landmarks/keypoints, parse/segment facial regions, align and crop faces (headshot / full face with hair & ears / head & shoulders), analyze face attributes, run face recognition, or deploy any of this locally on CPU/GPU/edge (incl. modest GPUs like an RTX 2060 6GB on Windows). The libraries are NOT vendored here — this skill tells you which to install and how to combine them.
metadata:
  type: authored
  origin: D:/Skills (authored 2026-10-19)
  domain: computer-vision / face
---

# Face detection & analysis — pipeline skill

A map of the face-CV ecosystem so you reach for the *right* tool at each stage instead of
defaulting to whatever you saw first. Nothing here is vendored; this skill tells you what to
`pip install` and how the pieces connect.

## When to use

Trigger on: detect faces, count faces, crop faces, bounding boxes, **facial landmarks /
keypoints**, 68-point / 468-point mesh, head pose, face **alignment**, **face parsing /
segmentation** (skin/eyes/hair/lips), face **attributes** (age, gender, emotion), **face
recognition / verification / embeddings**, face **preprocessing / augmentation**, and
**deploying** any of these on CPU, GPU, or edge.

## The pipeline (5 stages)

```
 raw image/video
      │
 1. DETECTION ───────► boxes + 5-pt landmarks   → references/detection.md
      │
 2. ALIGNMENT / LANDMARKS ─► 68 / 468 / 3D pts   → references/landmarks.md
      │
 3. PARSING / SEGMENTATION ─► per-pixel regions  → references/segmentation.md
      │
 (preprocessing & augmentation sit across 1–3)   → references/image-processing.md
      │
 4+5. INFERENCE & ACCELERATION (how you run 1–3)  → references/inference.md
```

Most tasks need only stages 1–2. Add 3 for masks/editing/beautify, and 4+5 when latency,
batch size, or edge/mobile matter.

## Building a face detect/align/crop module? → read the blueprint first

If the goal is a real **tool** (detect → pick primary face → align → segment → crop with
configurable styles, adaptive margins, aspect-ratio preservation, transparent bg, batch, QA,
tests & metrics), follow **[`references/crop-module-blueprint.md`](references/crop-module-blueprint.md)**.
It has the module layout, crop strategies (headshot / full-face-with-hair-&-ears / head-&-shoulders),
margin/alignment math, validation rules, pinned dependencies, run commands, and a recommended
lightweight stack for **Windows + RTX 2060 6 GB** (InsightFace `buffalo_s` + face-parsing ONNX via
ONNX Runtime CUDA, with CPU fallback). Core rules from it: never deform the face, never crop from a
fixed rectangle alone, preserve aspect ratio, handle borders/padding explicitly, and never claim
precision you haven't measured. Always inspect an existing project and match its architecture before
writing, and don't overwrite files without reading them.

## Decision guide — which library, by goal

| Your goal | First reach for | Why / fallback |
|---|---|---|
| Robust detection + recognition, production | **InsightFace** (SCRFD + ArcFace, ONNX) | SOTA accuracy, runs via ONNX Runtime. ⚠ model license (below) |
| Real-time / mobile / webcam, no GPU | **MediaPipe** | On-device, face mesh + blendshapes, Apache-2.0, trivial API |
| "Just give me faces" in one pip line | **RetinaFace** (serengil) or **uniface** | Simple detector-only wrappers |
| Attributes (age/gender/emotion/race) + easy recognition | **DeepFace** | Wraps many backends, one call per analysis |
| Dead-simple recognition, 68 landmarks, small project | **face_recognition** (dlib) | Easiest API; CPU-friendly; lower accuracy than InsightFace |
| Classic CV, Haar/DNN detector, you already use it | **OpenCV** | Ubiquitous; DNN face detector is decent, Haar is dated |
| Detect faces as one class among many objects | **Ultralytics YOLO** | Fast; YOLO-face weights exist. ⚠ **AGPL-3.0** |
| Precise 2D/3D landmarks (research-grade) | **face-alignment** (1adrianb) | FAN, 2D & 3D, good for alignment/3D |
| Per-pixel facial parts (skin, hair, eyes, lips…) | **face-parsing** (yakhyo, BiSeNet) | 19-class masks, ONNX |
| Arbitrary / promptable segmentation, video | **SAM2** (Meta) | When face-parsing classes aren't enough; promptable, tracks in video |
| Low-level face detector + 5pt, lightweight pip | **uniface** (yakhyo) | RetinaFace in a tidy package |

## Recommended default stacks

- **Accuracy-first (server/GPU):** InsightFace (detect+embed) → face-alignment (if you need
  dense/3D landmarks) → face-parsing or SAM2 (if you need masks), run through **ONNX Runtime**
  (CUDA) or **TensorRT**.
- **Real-time / edge / webcam:** MediaPipe end-to-end (detection + 468 mesh + blendshapes); if
  you must convert custom models, use **ONNX Runtime** or **OpenVINO**.
- **Quick prototype / notebook:** `face_recognition` or `DeepFace` — minimal code, CPU ok.

Preprocessing (resize, color, normalize) with **Pillow** / **OpenCV** / **scikit-image**;
training-time augmentation with **Albumentations** (it has keypoint- and mask-aware transforms —
keep landmarks/masks in sync with the image).

## Install cheat-sheet

```bash
# detection / recognition
pip install insightface onnxruntime            # add onnxruntime-gpu for CUDA
pip install mediapipe
pip install retina-face deepface               # serengil stack (TensorFlow under the hood)
pip install face_recognition                   # needs dlib; see dlib build notes
pip install ultralytics                         # YOLO — AGPL-3.0
pip install uniface

# landmarks / parsing / segmentation
pip install face-alignment
# face-parsing & SAM2: install from their GitHub repos (see references/)

# image processing & aug
pip install pillow scikit-image albumentations

# inference / acceleration
pip install onnxruntime            # or onnxruntime-gpu / onnxruntime-openvino
pip install torch torchvision      # see pytorch.org for the right CUDA build
pip install openvino
# TensorRT: install via NVIDIA (pip wheels or SDK), GPU-only
```

## ⚠ Licensing & model-usage cautions — read before shipping

- **Ultralytics YOLO is AGPL-3.0.** Using it in a network service can trigger copyleft on your
  whole app unless you hold a commercial license. Pick a different detector for closed-source SaaS.
- **InsightFace**: the *code* is MIT, but several **pretrained models are released for
  non-commercial / research use only.** Verify each model's license before commercial use.
- **dlib** is Boost (permissive) but the classic 68-point `shape_predictor` model and some
  datasets carry research-only terms.
- **MediaPipe, OpenCV, SAM2, OpenVINO** are Apache-2.0; **Pillow** HPND; **scikit-image**,
  **PyTorch**, **face-alignment** BSD; **Albumentations**, **ONNX Runtime**, **DeepFace**,
  **face_recognition**, **RetinaFace** MIT. **TensorRT** is an NVIDIA SDK (proprietary EULA; some
  components Apache).
- **Privacy / law**: face recognition and biometric data are regulated (GDPR/BIPA and similar).
  Get consent, minimize storage of embeddings, and check jurisdiction before deploying.

Always confirm the current license on each repo — terms change.

## References (open as needed)

- [`references/detection.md`](references/detection.md) — InsightFace, RetinaFace, MediaPipe, OpenCV, Ultralytics YOLO, DeepFace, face_recognition, dlib
- [`references/landmarks.md`](references/landmarks.md) — face-alignment (FAN), landmark_detection, MediaPipe Face Landmarker
- [`references/segmentation.md`](references/segmentation.md) — face-parsing (BiSeNet), uniface, SAM2
- [`references/image-processing.md`](references/image-processing.md) — Pillow, scikit-image, Albumentations
- [`references/inference.md`](references/inference.md) — ONNX Runtime, PyTorch, OpenVINO, TensorRT
- [`references/crop-module-blueprint.md`](references/crop-module-blueprint.md) — full build blueprint: modules, crop strategies, margins/alignment, validation/QA, pinned deps, tests & metrics, RTX 2060 6 GB stack

## Official docs

- OpenCV — https://docs.opencv.org/
- MediaPipe Face Landmarker — https://ai.google.dev/edge/mediapipe/solutions/vision/face_landmarker
- ONNX Runtime — https://onnxruntime.ai/docs/
- PyTorch — https://pytorch.org/docs/stable/
