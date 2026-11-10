# Preprocessing & augmentation (across stages 1–3)

Resize, color convert, normalize before a model; augment during training. Keep landmarks and
masks **in sync** with the image whenever you transform it.

## Pillow (PIL) — general imaging
- Repo: https://github.com/python-pillow/Pillow  ·  HPND (permissive)
- Load/save, resize, crop, color, draw. The everyday I/O library. `Image.open`, `.resize`,
  `.convert("RGB")`. Note: PIL is RGB; OpenCV is BGR — convert when mixing.

## scikit-image — scientific image processing
- Repo: https://github.com/scikit-image/scikit-image  ·  BSD
- Filters, morphology, color spaces, transforms, metrics (SSIM/PSNR), `img_as_float`. Use for
  analysis/measurement and non-DL processing; integrates with NumPy.

## Albumentations — fast augmentation (keypoint & mask aware)
- Repo: https://github.com/albumentations-team/albumentations  ·  MIT
- Training-time augmentation that transforms **image + bounding boxes + keypoints + masks
  together**, so your landmarks/parsing labels stay correct. Much faster than torchvision
  transforms for pipelines.
```python
import albumentations as A
tf = A.Compose(
    [A.HorizontalFlip(p=.5), A.RandomBrightnessContrast(p=.3), A.Affine(rotate=(-15,15), p=.5)],
    keypoint_params=A.KeypointParams(format="xy"),
    bbox_params=A.BboxParams(format="pascal_voc", label_fields=["cls"]),
)
out = tf(image=img, keypoints=lms, bboxes=boxes, cls=labels)
```

## Gotchas
- **Color order**: OpenCV = BGR, almost everything else = RGB. Convert explicitly.
- **Normalization**: match the model's expected mean/std and input size (e.g. ArcFace 112×112).
- **Don't flip landmarks naively**: a horizontal flip swaps left/right semantic points — use a
  library (Albumentations) or remap indices yourself.
- **Float vs uint8**: models want float32 (often 0–1 or normalized); displays want uint8 0–255.
