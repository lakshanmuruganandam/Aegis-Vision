# Aegis Vision
> **Real-Time YOLOv8 Object Detection & Tracking Core**  

Aegis Vision is an advanced, production-grade computer vision microservice built with **FastAPI** and the **Ultralytics YOLOv8** architecture. It features a premium, spatial glassmorphic UI and real-time inference telemetry.

## 🚀 Key Features

* **Real-Time Optical Engine:** Powered by YOLOv8s, achieving ultra-fast and highly accurate object detection and classification across 80 COCO classes.
* **Spatial Tracking integration:** Designed to support DeepSORT/ByteTrack methodologies for persistent entity tracking across frames.
* **Multi-Modal Input:** Capable of processing static image tensors, live webcam streams, and local video files seamlessly.
* **VisionOS UI Aesthetics:** A beautifully crafted, hardware-accelerated frontend featuring a sci-fi HUD overlay, dynamic bounding boxes, glowing brackets, and live terminal logging.
* **Real-time Telemetry:** Exposes latency (ms), FPS, and active entity counts instantly on the dashboard.

## 🛠 Tech Stack

* **Backend:** Python, FastAPI, Uvicorn, OpenCV, PyTorch, Ultralytics (YOLO)
* **Frontend:** HTML5, CSS3, TailwindCSS, Vanilla JavaScript, Canvas API
* **AI Models:** YOLOv8 (nano/small architectures)

## ⚙️ Installation & Usage

1. **Install Dependencies**
   Make sure you have Python 3.9+ installed.
   ```bash
   pip install -r requirements.txt
   ```
2. **Start the Neural Engine**
   ```bash
   python main.py
   ```
3. **Access the Interface**
   Open `http://localhost:8004` in your browser.

## 🧪 Evaluation

To run the automated verification script:
```bash
python run_eval.py
```
This tests core detection routes, tensor processing, bounding box generation, and API endpoints, outputting a success validation block.

---
*Architected and Engineered by Lakshan Muruganandam.*
