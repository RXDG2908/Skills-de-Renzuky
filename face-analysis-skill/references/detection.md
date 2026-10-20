# Stage 1 — Face detection (+ recognition / attributes)

Output of this stage: bounding boxes, usually 5-point landmarks (eyes, nose, mouth corners),
and optionally embeddings or attributes.

## InsightFace — SOTA detection + recognition
- Repo: https://github.com/deepinsight/insightface
- Detector **SCRFD**, recognizer **ArcFace**; ships `buffalo_l` / `buffalo_s` ONNX packs.
- Best accuracy in this list; runs on **ONNX Runtime** (CPU or CUDA).
- Code MIT; ⚠ **several pretrained models are non-commercial/research-only** — check per model.
```python
from insightface.app import FaceAnalysis
app = FaceAnalysis(name="buffalo_l")          # downloads models
app.prepare(ctx_id=0, det_size=(640, 640))     # ctx_id=-1 for CPU
faces = app.get(img_bgr)                        # .bbox .kps .embedding .age .sex
```

## RetinaFace (serengil) — simple, accurate detector
- Repo: https://github.com/serengil/retinaface  ·  `pip install retina-face`  ·  TensorFlow backend  ·  MIT
- Returns boxes + 5 landmarks + score. Good when you only need detection.
```python
from retinaface import RetinaFace
faces = RetinaFace.detect_faces("img.jpg")
```

## MediaPipe (Google) — real-time, on-device
- Repo: https://github.com/google-ai-edge/mediapipe  ·  Apache-2.0
- `FaceDetector` (fast boxes) and `FaceLandmarker` (468 mesh + blendshapes + head pose).
- CPU-friendly, mobile/web/desktop, great for webcam. See landmarks.md for mesh.

## OpenCV — classic + DNN
- Repo: https://github.com/opencv/opencv  ·  Docs: https://docs.opencv.org/  ·  Apache-2.0
- Haar cascades (fast, dated, many false positives) or the **DNN** face detector (res10 SSD /
  YuNet) which is much better. Use YuNet (`cv2.FaceDetectorYN`) for a modern, light detector.

## Ultralytics YOLO — detect faces as objects
- Repo: https://github.com/ultralytics/ultralytics  ·  ⚠ **AGPL-3.0** (commercial license needed for closed SaaS)
- Very fast; community **YOLOv8/YOLO11-face** weights give boxes (+keypoints on -pose variants).
```python
from ultralytics import YOLO
res = YOLO("yolov8n-face.pt")("img.jpg")
```

## DeepFace (serengil) — attributes + recognition wrapper
- Repo: https://github.com/serengil/deepface  ·  MIT
- One-call **age, gender, emotion, race** analysis and verification; wraps many backends
  (VGG-Face, Facenet, ArcFace, RetinaFace detector).
```python
from deepface import DeepFace
DeepFace.analyze("img.jpg", actions=["age","gender","emotion","race"])
DeepFace.verify("a.jpg", "b.jpg")
```

## face_recognition (ageitgey) — easiest recognition
- Repo: https://github.com/ageitgey/face_recognition  ·  MIT (built on dlib)
- Dead-simple API: locations, 68 landmarks, 128-d encodings. CPU ok; lower accuracy than
  InsightFace. Needs dlib installed.
```python
import face_recognition as fr
locs = fr.face_locations(img); enc = fr.face_encodings(img, locs)
```

## dlib (davisking) — the engine under many of the above
- Repo: https://github.com/davisking/dlib  ·  Boost license (⚠ some bundled models research-only)
- HOG (CPU) and CNN (GPU) detectors + 68-point `shape_predictor`. Building can need CMake + a
  C++ toolchain; on Windows prefer prebuilt wheels.

## Choosing fast
- Need best accuracy / embeddings → **InsightFace**.
- Need real-time on-device → **MediaPipe**.
- Need attributes in one call → **DeepFace**.
- Prototyping / tiny project → **face_recognition**.
- Already in an OpenCV pipeline → **YuNet** via OpenCV DNN.
- Multi-object scene where face is one class → **YOLO** (mind AGPL).
