# Stage 2 — Alignment & landmarks

Output: dense keypoints (68 / 468 / 3D), used to **align** a face (warp to a canonical pose so
recognition/parsing behave) and to drive geometry (head pose, expression, AR, beautify).

## face-alignment (1adrianb) — FAN, 2D & 3D
- Repo: https://github.com/1adrianb/face-alignment  ·  BSD-3  ·  PyTorch
- Research-grade 2D **and 3D** landmarks (the "how far can we go" FAN work). Use when you need
  3D points or robust dense landmarks for alignment.
```python
import face_alignment
fa = face_alignment.FaceAlignment(face_alignment.LandmarksType.TWO_D, device="cuda")
preds = fa.get_landmarks("img.jpg")   # list of (68,2) arrays
```

## MediaPipe Face Landmarker — 468 mesh + blendshapes
- Docs: https://ai.google.dev/edge/mediapipe/solutions/vision/face_landmarker
- 468 3D mesh points, 52 **blendshape** scores (expression coefficients), and a facial
  transformation matrix (head pose). Real-time, on-device. Best choice for AR / avatars /
  expression capture and anything live.

## landmark_detection (sneha-cornell)
- Repo: https://github.com/sneha-cornell/landmark_detection
- Smaller research/educational repo for landmark detection. Treat as a reference implementation /
  learning resource rather than a maintained production package — verify its model, license, and
  input format before relying on it; prefer face-alignment or MediaPipe for production.

## dlib 68-point (via face_recognition or dlib directly)
- Lightweight CPU landmarks; fine for alignment when you don't need 3D. See detection.md.

## Alignment recipe
1. Detect face + get landmarks (5-pt from InsightFace is enough for similarity-transform align).
2. Compute an affine/similarity transform mapping the eyes/mouth to canonical positions.
3. Warp with OpenCV (`cv2.warpAffine`) to a fixed size (e.g. 112×112 for ArcFace).
InsightFace does this internally; do it yourself only when feeding a custom recognizer.

## Choosing fast
- Live / AR / expression → **MediaPipe Face Landmarker** (mesh + blendshapes).
- 3D or dense research landmarks → **face-alignment**.
- Just enough to align a crop → 5-pt from your detector, or dlib 68-pt.
