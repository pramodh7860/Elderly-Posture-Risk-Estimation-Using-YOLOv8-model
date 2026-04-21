# utils.py
import cv2

def draw_pose(frame, keypoints, label=None, color=(0, 255, 0)):
    """Draw keypoints and risk label."""
    for x, y in keypoints:
        cv2.circle(frame, (int(x), int(y)), 4, color, -1)

    if label:
        cv2.putText(frame, label, (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
    return frame