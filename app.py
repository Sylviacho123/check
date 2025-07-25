from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# 預設物品對應（與前端勾選 value 對應）
ITEMS = ["手機", "錢包", "鑰匙", "行動電源", "帆布袋", "水壺", "眼鏡"]

@app.route('/')
def index():
    return render_template('index.html')  # 你的HTML放這檔名

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "沒有上傳檔案"
    file = request.files['file']
    if file.filename == '':
        return "沒有選擇檔案"

    selected_items = request.form.getlist('items')  # 取得勾選的物品列表

    # 存檔
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # 這裡接入你的物件檢測程式碼，目前模擬結果：
    # 假設都找到，實際你會呼叫YOLO或其他模型做檢測
    detected = []
    for item in selected_items:
        detected.append({'item': item, 'found': True})

    return render_template('result.html', filename=file.filename, detected=detected, selected=selected_items)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

