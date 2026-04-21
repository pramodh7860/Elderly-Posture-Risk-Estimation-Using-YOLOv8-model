# 👵 Elderly Pose Risk Detection using YOLOv8

## 🧩 Overview
This project detects and analyzes the posture of elderly people using **YOLOv8 Pose Estimation**.  
It identifies body keypoints and classifies posture into three categories:
- ✅ **Normal** — Standing or safe position  
- ⚠️ **Risky** — Leaning, imbalance, or unsafe angle detected  
- 🚨 **Critical** — Fall or lying position detected  

When a risky or critical posture is detected, the system automatically plays an alert sound to warn nearby caregivers.

---

## 🧠 Features
- YOLOv8-based keypoint pose detection  
- Automatic posture classification (Normal / Risky / Critical)  
- Real-time or image-based analysis  
- Alert system for unsafe postures  
- Visual output with pose skeleton and color-coded labels  

---

## 🧰 Tech Stack
- **Python 3.10+**
- **OpenCV** – Image processing and display  
- **Ultralytics YOLOv8** – Pose estimation model  
- **NumPy** – Keypoint data handling  
- **pygame** (or `os.system` for alerts) – Audio alert system  

---

## ⚙️ Output

![Elderly Posture Demo](posture.jpeg)
![Elderly Posture Demo](postureop.png)



   
