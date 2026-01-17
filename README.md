# Smart Scene Analyzer

A professional Computer Vision project that performs object detection and segmentation
on images using YOLOv8 and OpenCV.

## 🔍 Features
- Object Detection using YOLOv8
- Semantic Segmentation
- Image processing with OpenCV
- Modular & clean code structure

## 🛠 Tech Stack
- Python
- OpenCV
- YOLOv8
- PyTorch

## 📂 Project Structure
smart-scene-analyzer/
│
├── data/
│   ├── images/
│   │   └── sample.jpg
│   └── videos/
│       └── sample.mp4
│
├── models/
│   └── yolov8n.pt
│
├── src/
│   ├── detect.py
│   ├── segment.py
│   └── utils.py
│
├── outputs/
│   ├── images/
│   └── videos/
│
├── requirements.txt
├── README.md
└── .gitignore

## ▶️ How to Run
```bash
pip install -r requirements.txt
python src/detect.py
python src/segment.py
