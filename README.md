# **Custom YOLOv8 Face Detection**

This project is a custom-trained **YOLOv8** object detection model designed to recognize a single face — mine — using a small, manually-labeled dataset.  
It supports **real-time detection** via webcam as well as inference on static images and videos.

---

## Features
- **Custom dataset** with labeled images and bounding boxes.
- **Real-time detection** from webcam feed.
- **Configurable confidence threshold** for improved accuracy.
- Easy to retrain with your own images.
- **Dataset excluded** from repo via `.gitignore` for privacy.

---

## Project Structure
Face_detection/
│
├── data/ # Contains images and labels (excluded from repo)
│ ├── images/
│ └── labels/
│
├── runs/ # YOLO training results (auto-generated)
│
├── yolonewenv/ # Virtual environment (excluded from repo)
│
├── yolov8n.pt # Base YOLO model weights
├── config.yaml # Dataset config for YOLO
├── face_detector.py # Training script
├── checking.py # Webcam/image testing script
├── .gitignore # Ignore sensitive files
└── README.md # Project documentation

## Setup 

1. **Clone the repository**
```bash
git clone https://github.com/dhiren101-dotcom/Face_Detection.git
cd Face_Detection

2. **Create and activate a virtual environment**
python3 -m venv yolonewenv
source yolonewenv/bin/activate 

3. **Installing Dependancies**
pip install ultralytics opencv-python


## Training

**To train the model** : 
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.train(data="config.yaml", epochs=50, imgsz=640)

## Inference 

Run Webcam detection : 
from ultralytics import YOLO

model = YOLO("runs/detect/trainX/weights/best.pt")
model.predict(source=0, conf=0.45, show=True)

For an image: 
model.predict(source="path/to/image.jpg", conf=0.45, show=True)


##Important Notes 
---The data/images folder is not included in the repository for privacy.
---You can replace my dataset with your own by updating config.yaml and retraining.










