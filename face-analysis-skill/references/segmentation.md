# Stage 3 — Parsing & segmentation

Output: per-pixel masks. **Face parsing** = fixed semantic classes (skin, nose, eyes, brows,
lips, hair, …). **Segmentation (SAM2)** = arbitrary/promptable masks, including video tracking.
Use for editing, beautify, makeup/try-on, background/hair effects, masking for inpainting.

## face-parsing (yakhyo) — BiSeNet, 19 classes
- Repo: https://github.com/yakhyo/face-parsing  ·  BiSeNet-based  ·  ONNX export available
- Classic 19-class face parsing (CelebAMask-HQ labels: skin, l/r eye, l/r brow, nose, mouth,
  u/l lip, hair, hat, ear, neck, cloth, …). Fast, deterministic classes — ideal for makeup,
  skin retouch, hair recolor. Install from the repo; run via PyTorch or ONNX Runtime.

## uniface (yakhyo) — lightweight detection + landmarks
- Repo: https://github.com/yakhyo/uniface  ·  pip-installable
- Tidy RetinaFace-style package giving boxes + 5-pt landmarks (a Stage-1 helper, grouped here as
  part of yakhyo's face toolkit). Use it to get the crop you then parse.
```python
from uniface import RetinaFace
det = RetinaFace(); boxes, kps = det.detect(img)
```

## SAM2 (Meta) — Segment Anything 2, promptable + video
- Repo: https://github.com/facebookresearch/sam2  ·  Apache-2.0
- When fixed parsing classes aren't enough: promptable masks from a point/box, and **mask
  tracking across video frames**. Heavier; GPU recommended. Great for "segment exactly this
  region" or temporally consistent masks in clips.
```python
from sam2.sam2_image_predictor import SAM2ImagePredictor
predictor = SAM2ImagePredictor.from_pretrained("facebook/sam2-hiera-large")
predictor.set_image(img); masks, _, _ = predictor.predict(point_coords=pts, point_labels=lbls)
```

## Choosing fast
- Need named facial parts (skin/hair/lips…) → **face-parsing** (BiSeNet).
- Need an arbitrary region, or masks that track through video → **SAM2**.
- Just need the face crop to parse → detect with **uniface** / InsightFace first.
