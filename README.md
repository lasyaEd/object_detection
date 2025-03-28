# object_detection

# 🚗 Highway Vehicle Detection & Tracking with YOLOv4 + SORT

This project performs real-time object detection and multi-object tracking on highway traffic footage. It uses **YOLOv4** for object detection and **SORT (Simple Online Realtime Tracking)** for assigning persistent tracking IDs to vehicles.

---
## ⚙️ Requirements

Install dependencies using:

```bash
pip install opencv-python numpy filterpy
```
(You do not need skimage — remove the import if you cloned sort.py from GitHub.)

🧠 How It Works
object_detection.py loads YOLOv4 using OpenCV's dnn module

object_tracking.py runs the pipeline:

Detects objects in each frame

Filters only car, truck, bus, motorbike classes

Passes bounding boxes to the SORT tracker

Draws tracked boxes and unique track IDs on vehicles



📦 Resources
YOLOv4 Weights

SORT Tracker (Abewley GitHub)
