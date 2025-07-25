from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # 載入官方預訓練模型

model.train(data='data.yaml', epochs=50, imgsz=640, batch=16)
