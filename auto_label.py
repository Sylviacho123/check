# auto_label.py
from ultralytics import YOLO
import cv2
import os
from glob import glob

# 載入預訓練模型
model = YOLO('yolov8n.pt')

# 你的類別名稱（照你圖片資料順序）
class_names = ['phone', 'wallet', 'key', 'powerbank', 'bag', 'bottle', 'glasses']
name_to_index = {name: i for i, name in enumerate(class_names)}

# 要標註的圖片路徑（train 與 val）
for split in ['train', 'val']:
    img_dir = f'dataset/images/{split}'
    label_dir = f'dataset/labels/{split}'
    os.makedirs(label_dir, exist_ok=True)

    for img_path in glob(f'{img_dir}/*.jpg'):
        results = model(img_path)[0]
        h, w = cv2.imread(img_path).shape[:2]

        # 產生標註檔名
        label_path = os.path.join(label_dir, os.path.basename(img_path).replace('.jpg', '.txt'))
        with open(label_path, 'w') as f:
            for r in results.boxes.data:
                cls_id = int(r[5].item())  # 原模型類別 ID
                cls_name = model.names[cls_id].lower()
                if cls_name in name_to_index:
                    x1, y1, x2, y2 = r[0:4]
                    cx = ((x1 + x2) / 2) / w
                    cy = ((y1 + y2) / 2) / h
                    bw = (x2 - x1) / w
                    bh = (y2 - y1) / h
                    f.write(f"{name_to_index[cls_name]} {cx:.6f} {cy:.6f} {bw:.6f} {bh:.6f}\n")
