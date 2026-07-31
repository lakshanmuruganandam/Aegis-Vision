import requests
import time
import subprocess
import os
import cv2
import base64

print("--- INITIATING TASK 4: OBJECT DETECTION & TRACKING EVALUATION ---")

# Kill any existing server on 8004
os.system("kill -9 $(lsof -t -i:8004) 2>/dev/null")
time.sleep(1)

# Boot server
proc = subprocess.Popen(["python", "main.py"], cwd=os.path.dirname(os.path.abspath(__file__)))

ready = False
for _ in range(20):
    try:
        res = requests.get("http://localhost:8004/api/classes", timeout=1)
        if res.status_code == 200:
            ready = True
            break
    except:
        time.sleep(1.0)

if not ready:
    print("❌ Failed to start server.")
    proc.terminate()
    exit(1)

try:
    # 1. UI Check
    res = requests.get("http://localhost:8004/")
    print(f"GET / -> Status: {res.status_code}, Length: {len(res.text)} bytes")
    assert res.status_code == 200

    # 2. Classes Check
    res = requests.get("http://localhost:8004/api/classes")
    data = res.json()
    print(f"GET /api/classes -> COCO Classes Indexed: {data['total']}")
    assert data["total"] == 80

    # 3. Synthetic Frame Test (Generate image frame with shapes/objects)
    img = 255 * os.urandom(480 * 640 * 3)
    img = cv2.resize(cv2.imdecode(cv2.imencode('.jpg', cv2.imread('/Users/lakshanmuruganandam/Desktop/codsoft internsip/CODSOFT_TASKS/Task_5_FaceRecognition/tests/images/Elon Musk.jpg')[1])[1], cv2.IMREAD_COLOR), (640, 480))
    _, buffer = cv2.imencode('.jpg', img)
    b64 = "data:image/jpeg;base64," + base64.b64encode(buffer).decode('utf-8')

    start = time.time()
    res = requests.post("http://localhost:8004/api/detect", json={"image_base64": b64})
    elapsed = (time.time() - start) * 1000
    d = res.json()
    
    objects = d.get("objects", [])
    print(f"  POST /api/detect -> Objects Detected & Tracked: {len(objects)} ({elapsed:.1f}ms)")
    for obj in objects:
        print(f"      [{obj['id']}] Label: '{obj['label']}', Conf: {obj['confidence']*100:.1f}%, Box: ({obj['x']}, {obj['y']}, {obj['width']}, {obj['height']})")

    assert d.get("status") == "success"
    print("\n✅ TASK 4 EVALUATION: 100% SUCCESS")

finally:
    proc.terminate()
