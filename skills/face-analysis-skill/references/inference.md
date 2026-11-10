# Stages 4+5 — Inference & acceleration

*How* you run the models from stages 1–3. Pick a runtime for your hardware and latency budget.

## ONNX Runtime — the portable default
- Repo: https://github.com/microsoft/onnxruntime  ·  Docs: https://onnxruntime.ai/docs/  ·  MIT
- Runs ONNX models across **CPU, CUDA, DirectML, OpenVINO, TensorRT, CoreML** via *execution
  providers*. InsightFace and face-parsing already ship/export ONNX, so this is the usual choice.
```python
import onnxruntime as ort
sess = ort.InferenceSession("model.onnx", providers=["CUDAExecutionProvider","CPUExecutionProvider"])
out = sess.run(None, {sess.get_inputs()[0].name: x})
```
- Install: `onnxruntime` (CPU), `onnxruntime-gpu` (CUDA), `onnxruntime-openvino` (Intel).

## PyTorch — training & research runtime
- Repo: https://github.com/pytorch/pytorch  ·  Docs: https://pytorch.org/docs/stable/  ·  BSD
- Native runtime for face-alignment, SAM2, YOLO, most research models. Use `torch.no_grad()`,
  `half()`/`autocast` for speed, and export to ONNX (`torch.onnx.export`) for deployment.
- Install the build matching your CUDA from pytorch.org — don't just `pip install torch` blind
  on GPU boxes.

## OpenVINO (Intel) — CPU / iGPU / NPU acceleration
- Repo: https://github.com/openvinotoolkit/openvino  ·  Apache-2.0
- Optimizes inference on Intel CPUs, integrated GPUs, and NPUs; converts ONNX/TF/PyTorch models.
  Best when you're deploying on Intel hardware without a discrete NVIDIA GPU. Can also be an ONNX
  Runtime execution provider.

## TensorRT (NVIDIA) — max GPU throughput
- Repo: https://github.com/NVIDIA/TensorRT  ·  NVIDIA SDK (proprietary EULA; some OSS parts Apache)
- Lowest latency / highest throughput on NVIDIA GPUs via kernel fusion + FP16/INT8. More setup
  (engine build per GPU/precision). Reach for it only when ONNX Runtime-CUDA isn't fast enough.
  Often used through ONNX Runtime's TensorRT execution provider to avoid raw TRT API.

## Choosing fast
- Portable, mixed hardware, already have ONNX → **ONNX Runtime** (+ the right provider).
- Training / research / model not yet exported → **PyTorch**.
- Intel-only deployment (no NVIDIA GPU) → **OpenVINO**.
- Squeeze every ms on NVIDIA GPUs → **TensorRT** (ideally via ORT's TRT provider).

## Perf checklist
- Quantize / use FP16 or INT8 where accuracy allows.
- Batch requests; keep the session/engine warm (don't rebuild per call).
- Pin input size; preallocate buffers; avoid CPU↔GPU copies in the hot loop.
- Benchmark end-to-end (pre+infer+post), not just the model forward pass.
