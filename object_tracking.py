import cv2
import numpy as np
from object_detection import ObjectDetection
from sort import Sort  # NEW: import SORT tracker

# Initialize object detection
od = ObjectDetection()
vehicle_classes = ["car", "truck", "bus", "motorbike"]

# Initialize SORT tracker
tracker = Sort(max_age=5, min_hits=3, iou_threshold=0.3)

# Load video
cap = cv2.VideoCapture("los_angeles.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detections = []

    # Detect objects
    class_ids, scores, boxes = od.detect(frame)

    for class_id, score, box in zip(class_ids, scores, boxes):
        class_name = od.classes[class_id]
        if class_name in vehicle_classes:
            x, y, w, h = box
            # Convert to [x1, y1, x2, y2, score] format for SORT
            detections.append([x, y, x + w, y + h, float(score)])

    # Convert to numpy array
    detections_np = np.array(detections)
    if len(detections_np) == 0:
        detections_np = np.empty((0, 5))

    # Update tracker
    tracks = tracker.update(detections_np)

    # Draw tracks
    for track in tracks:
        x1, y1, x2, y2, track_id = track.astype(int)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f'ID {track_id}', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
