# object_detection

# 🚗 Highway Vehicle Detection & Tracking with YOLOv4 + SORT

This project performs real-time object detection and multi-object tracking on highway traffic footage. It uses **YOLOv4** for object detection and **SORT (Simple Online Realtime Tracking)** for assigning persistent tracking IDs to vehicles.

---

## 📁 Project Structure

. ├── object_tracking.py # Main script to run detection + tracking ├── object_detection.py # Wrapper for OpenCV YOLOv4 object detection ├── sort.py # SORT tracker implementation ├── dnn_model/ │ ├── yolov4.cfg # YOLOv4 config file │ ├── yolov4.weights # 🔺 Required - see below │ └── classes.txt # COCO class labels ├── los_angeles.mp4 # Input highway video └──


---

## ⚙️ Requirements

Install dependencies using:

```bash
pip install opencv-python numpy filterpy

(You do not need skimage — remove the import if you cloned sort.py from GitHub.)

🧠 How It Works
object_detection.py loads YOLOv4 using OpenCV's dnn module

object_tracking.py runs the pipeline:

Detects objects in each frame

Filters only car, truck, bus, motorbike classes

Passes bounding boxes to the SORT tracker

Draws tracked boxes and unique track IDs on vehicles

▶️ Usage
Make sure you have the YOLOv4 files (yolov4.cfg, yolov4.weights, and classes.txt) in the dnn_model/ folder.
Run the tracking script:

bash
Copy
Edit
python object_tracking.py
💾 Optional: Save Output
To save the output video, add a cv2.VideoWriter to your script. Let us know if you'd like help setting this up!

📦 Resources
YOLOv4 Weights

SORT Tracker (Abewley GitHub)
