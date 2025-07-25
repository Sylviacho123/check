import os
import shutil
import random

src_dir = 'images_raw'  # 原始圖片資料夾，裡面有子資料夾
train_img_dir = 'dataset/images/train'
val_img_dir = 'dataset/images/val'
train_label_dir = 'dataset/labels/train'
val_label_dir = 'dataset/labels/val'

os.makedirs(train_img_dir, exist_ok=True)
os.makedirs(val_img_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# 遞迴抓所有子資料夾的圖片檔（jpg、png）
images = []
for root, dirs, files in os.walk(src_dir):
    for file in files:
        if file.lower().endswith(('.jpg', '.png')):
            images.append(os.path.join(root, file))

random.shuffle(images)

split_idx = int(len(images) * 0.8)
train_images = images[:split_idx]
val_images = images[split_idx:]

# 定義複製函數，保持圖片檔名不變（或改名避免重複）
def copy_images(img_paths, dest_img_dir, dest_label_dir):
    for img_path in img_paths:
        img_name = os.path.basename(img_path)
        shutil.copy(img_path, os.path.join(dest_img_dir, img_name))

        label_name = os.path.splitext(img_name)[0] + '.txt'
        src_label = os.path.join(os.path.dirname(img_path), label_name)
        if os.path.exists(src_label):
            shutil.copy(src_label, os.path.join(dest_label_dir, label_name))

copy_images(train_images, train_img_dir, train_label_dir)
copy_images(val_images, val_img_dir, val_label_dir)

print(f"總共圖片數量: {len(images)}")
print(f"訓練集: {len(train_images)} 張")
print(f"驗證集: {len(val_images)} 張")
print("資料分割完成")
