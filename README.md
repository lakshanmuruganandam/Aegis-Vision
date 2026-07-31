<div align="center">
  <img src="https://img.shields.io/badge/Aegis-Vision-0f172a?style=for-the-badge&logo=ultralytics" alt="Aegis Vision Banner">
  <h1>Aegis Vision ✦</h1>
  <p><b>Real-Time YOLOv8 Object Detection & Tracking Core</b></p>
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
  [![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)]()
  [![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
  [![Status](https://img.shields.io/badge/Status-Production_Ready-success.svg)]()
</div>

---

## 🚀 The Vision

High-speed computer vision systems traditionally require massive cloud GPU clusters, sending massive amounts of video data over the network. **Aegis Vision** changes this paradigm by running a highly optimized YOLOv8 instance directly at the edge/on-premise.

Designed for security feeds, autonomous robotics, and real-time telemetry, Aegis extracts entity data in milliseconds—identifying objects and tracking their trajectories without ever sending pixels to external servers. This is zero-trust computer vision.

---

## 🏆 Unmatched Performance: Competitive Analysis

Aegis Vision provides the bleeding-edge accuracy of heavy convolutional networks, but runs at a fraction of the computational cost.

| Feature | Aegis Vision (Ours) | Cloud Vision APIs | OpenCV Haar Cascades | Legacy YOLOv3 |
|---------|---------------------|-------------------|----------------------|---------------|
| **Inference Speed**| **Ultra-Fast (Real-Time)** | Slow (Network Bound)| Fast | Medium |
| **Accuracy (mAP)** | **State-of-the-Art (YOLOv8)**| High | Poor | Medium |
| **Data Sovereignty** | **100% On-Premise** | Stored in Cloud | On-Premise | On-Premise |
| **Cost Per Frame**| **$0.00** | Highly Expensive | $0.00 | $0.00 |
| **Tracking** | **DeepSORT/ByteTrack** | Varies | None | None |

---

## 🧠 Core Architecture & System Flow

```mermaid
graph TD
    A["Client UI (Web / Camera)"] -->|"POST Base64 Frame"| B("FastAPI Vision Gateway")
    B --> C{"OpenCV Tensor Normalization"}
    C -->|"Ultralytics YOLOv8s"| D["Entity Detection (80 COCO Classes)"]
    D --> E["Bounding Box & Confidence Extraction"]
    E --> F{"DeepSORT / ByteTrack Integration"}
    F --> G["Persistent Object IDs"]
    G --> H["Canvas Rendering Overlay & Data Feed"]
    H --> I["JSON Analytics Payload (Latency, FPS, Count)"]
    I --> A
```

### 1. Neural Optical Detection
Aegis utilizes Ultralytics YOLOv8, effectively skipping the bottlenecks of anchor-based systems to provide anchor-free object detection. This results in far fewer false positives and significantly faster NMS (Non-Maximum Suppression) processing times.

### 2. High-Speed Telemetry
The UI parses a live REST/WebSocket stream, overlaying geometric glowing bounding boxes via the HTML5 Canvas API while logging raw telemetry (confidence intervals, object labels, bounding box coordinates) in a terminal-style data feed.

---

## 📂 Project Structure & Files

```text
Aegis-Vision/
├── main.py                 # Core FastAPI Server & Endpoint Routing
├── tracker.py              # YOLOv8 Inference & Canvas Draw Logic
├── yolov8n.pt              # Neural Weights (Nano Architecture)
├── index.html              # VisionOS-inspired Sci-Fi HUD
├── requirements.txt        # Python Dependencies
├── tests/
│   ├── run_eval.py         # End-to-end tensor verification
│   ├── test_api.py         # Unit tests for API endpoints
│   └── test_vision.py      # Unit tests for OpenCV manipulation
├── demo_assets/            # Screenshots and architectural diagrams
├── CONTRIBUTING.md         # Guidelines for OSS contributions
└── LICENSE                 # MIT License
```

---

## 🔌 API Reference

### `POST /detect`
Processes a base64 encoded image frame and returns bounding boxes.

**Headers:**
- `Content-Type: application/json`

**Payload:**
```json
{
  "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAAAAAA..."
}
```

**Response (200 OK):**
```json
{
  "detections": [
    {
      "label": "person",
      "confidence": 0.98,
      "box": [120, 45, 300, 400]
    }
  ],
  "latency_ms": 12.4
}
```

---

## ⚙️ Installation & Deployment

### Prerequisites
- Python 3.9+
- OpenCV, Ultralytics, PyTorch, FastAPI

### Local Development Start
```bash
# 1. Clone the repository
git clone https://github.com/lakshanmuruganandam/Aegis-Vision.git
cd Aegis-Vision

# 2. Install dependencies
pip install -r requirements.txt

# 3. Boot the Optical Engine
python main.py
```
*The UI Dashboard will be available at `http://localhost:8004/`.*

### Docker Deployment (Production)
```bash
docker build -t aegis-vision .
docker run -p 8004:8004 --gpus all aegis-vision
```

---

## 🤝 Contributing
We welcome enterprise integrations and OSS contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 📜 License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---
<div align="center">
  <b>Seeing the unseen. Engineered by Lakshan Muruganandam.</b>
</div>
