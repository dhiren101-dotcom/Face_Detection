from ultralytics import YOLO

model = YOLO("runs/detect/train5/weights/best.pt")  
new_results = model.predict(source=0, conf=0.45,show=True)



