from flask import Flask, render_template, request, redirect, url_for
import os
from ultralytics import YOLO
from PIL import Image
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['RESULT_FOLDER'] = 'static/results/'

# Klasörler yoksa oluştur
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

# Modeli yükle
MODEL_PATH = "runs/detect/train2/weights/best.pt"
model = YOLO(MODEL_PATH)

# Tespit edilen plaka sayacı (bellekte tutulur)
detected_plate_count = 0

def predict_image(img_path, result_path):
    results = model(img_path)
    results[0].save(filename=result_path)
    # Plaka tespit edildi mi?
    try:
        n = len(results[0].boxes)
    except Exception:
        n = 0
    return result_path, n

@app.route('/', methods=['GET', 'POST'])
def index():
    global detected_plate_count
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[-1]
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(upload_path)
            # Tahmin yap
            result_filename = filename.replace('.', '_result.')
            result_path = os.path.join(app.config['RESULT_FOLDER'], result_filename)
            result_path, n = predict_image(upload_path, result_path)
            detected_plate_count += n
            return render_template('result.html', result_image=result_filename, original_image=filename, detected_plate_count=detected_plate_count, detected_count=n)
    return render_template('index.html', detected_plate_count=detected_plate_count)

@app.route('/result/<result_image>/<original_image>')
def result(result_image, original_image):
    global detected_plate_count
    # Sonuç sayfasında da sayaç ve tespit edilen plaka sayısı gösterilsin
    return render_template('result.html', result_image=result_image, original_image=original_image, detected_plate_count=detected_plate_count)

@app.route('/about')
def about():
    global detected_plate_count
    return render_template('about.html', detected_plate_count=detected_plate_count)

if __name__ == '__main__':
    app.run(debug=True) 