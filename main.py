# main_image.py
from ultralytics import YOLO
import cv2
import os
from risk_analysis import assess_posture
from utils import draw_pose

# Load YOLO pose model
pose_model = YOLO('yolov8n-pose.pt')

# Path to image
image_path = 'posture.jpeg'  # change this to your image filename

# Read image
frame = cv2.imread(image_path)
if frame is None:
    raise FileNotFoundError(f"Image not found at {image_path}")

# Run YOLO pose detection
results = pose_model.predict(source=frame, conf=0.5, verbose=False)

for r in results:
    if r.keypoints is not None:
        keypoints = r.keypoints.xy[0].cpu().numpy()
        label = assess_posture(keypoints)

        # Color based on risk
        color = (0, 255, 0) if label == "Normal" else (0, 255, 255) if label == "Risky" else (0, 0, 255)

        # Alert sound using system command (instead of playsound)
        if label in ["Risky", "Critical"]:
            try:
                # macOS / Linux
                os.system("afplay alert.mp3")  # or `aplay alert.mp3` for Linux
            except Exception as e:
                print("Alert sound error:", e)

        # Draw pose and label
        frame = draw_pose(frame, keypoints, label, color)

# Display the output image
cv2.imshow("Elder Pose Risk Estimation", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Optionally save result
cv2.imwrite("output_pose_estimation.jpg", frame)
print("Output saved as output_pose_estimation.jpg")