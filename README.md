# Real-Time Object Detection

## 📌 Overview

This project is a real-time object detection application built with **Python**, **OpenCV**, and **YOLO11**.

It is a personal learning project focused on studying computer vision, OpenCV, and YOLO through hands-on implementation.

---

## ✨ Features

- Webcam preview using OpenCV
- Image object detection using YOLO11
- Save detection results as an image
- Real-time object detection using webcam

---

## 🛠 Tech Stack

- Python
- OpenCV
- Ultralytics YOLO11

---

## 📁 Project Structure

```text
realtime-object-detection/
├── camera_test.py
├── image_detection.py
├── realtime_detection.py
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

| File | Purpose |
|------|---------|
| `camera_test.py` | Test file for OpenCV webcam |
| `image_detection.py` | Test file for YOLO image detection |
| `realtime_detection.py` | Main real-time object detection application |

---

## 🚫 Ignored Files

The following files and directories are excluded from GitHub using `.gitignore`.

- `.venv/`
- `__pycache__/`
- `*.pyc`
- `.DS_Store`
- `yolo11n.pt`
- `results.jpg`
- `images/` (temporary test images)

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run real-time detection

```bash
python realtime_detection.py
```

Press **q** to exit.

---

## 🚀 Future Plans

- Display confidence score
- Detect specific objects only
- Count detected objects
- Display FPS
- Performance optimization

---

## 👤 Author

GitHub: ppseeeheee