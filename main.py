import cv2
import base64
import numpy as np
import time
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ultralytics import YOLO
from tracker import EuclideanTracker

app = FastAPI(title="Aegis Vision | YOLOv8 Neural Object Detection & Tracking Core")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load lightweight YOLOv8 Nano model
print("[Aegis Vision] Loading YOLOv8 Neural Network Model...")
yolo_model = YOLO("yolov8n.pt")
tracker = EuclideanTracker()

class FrameRequest(BaseModel):
    image_base64: str

@app.get("/api/classes")
async def get_classes():
    return {"classes": list(yolo_model.names.values()), "total": len(yolo_model.names)}

@app.post("/api/detect")
async def detect_and_track_objects(req: FrameRequest):
    if not req.image_base64:
        raise HTTPException(status_code=400, detail="Frame data cannot be empty.")
    
    start_time = time.time()
    
    try:
        # Decode Base64 frame
        img_data = base64.b64decode(req.image_base64.split(",")[1])
        nparr = np.frombuffer(img_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if frame is None:
            return {"status": "error", "message": "Failed to decode video frame."}
            
        # Run YOLOv8 Detection
        results = yolo_model(frame, verbose=False)[0]
        
        rects = []
        for box in results.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            conf = float(box.conf[0])
            cls_id = int(box.cls[0])
            label = yolo_model.names[cls_id]
            
            if conf >= 0.35: # Confidence filter threshold
                w = int(x2 - x1)
                h = int(y2 - y1)
                rects.append([int(x1), int(y1), w, h, label.upper(), round(conf, 2)])
                
        # Apply Euclidean Tracking to assign IDs
        tracked_objects = tracker.update(rects)
        
        execution_ms = round((time.time() - start_time) * 1000, 1)
        fps = round(1000.0 / max(execution_ms, 1.0), 1)
        
        return {
            "status": "success",
            "objects": tracked_objects,
            "telemetry": {
                "model": "YOLOv8n + IoU Tracker",
                "execution_ms": f"{execution_ms}ms",
                "fps": fps,
                "objects_found": len(tracked_objects)
            }
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8004)
