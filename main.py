# Transfer Learning.


# ....

from ultralytics import YOLO
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import os


def train():
    model = YOLO("yolov8n.pt")
  #  model.train(data="data.yaml", epochs=10, imgsz=640, batch=8)
    #1955/8

# Pythondaki main method.
# python main.py => Çalış
# başka bir dosyadan import edildiğinde çalışmaz.
if __name__ == "__main__":
    train()


# Eğitimi bitirelim.
# Oluşan klasörü inceleyelim. 
# İçerisindeki "best.pt" dosyasını kullanacağız.
# Bu pt dosyası ile birlikte tahmin yapacak yeni bir dosyada bir GUI uygulama yapalım.
# 20:30

# Modeli yükle (best.pt dosyanın yolunu güncelle)
MODEL_PATH = "runs/detect/train2/weights/best.pt"
model = YOLO(MODEL_PATH)

#tahmin yapma
def predict_image(img_path):
    results = model(img_path)
    # Sonuç görselini kaydet
    result_img_path = "result.jpg"
    results[0].save(filename=result_img_path)
    return result_img_path
#görsel seçme
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if not file_path:
        return
    # Tahmin yap
    result_img_path = predict_image(file_path)
    # Sonucu göster
    img = Image.open(result_img_path)
    img = img.resize((400, 400))
    img_tk = ImageTk.PhotoImage(img)
    panel.config(image=img_tk)
    panel.image = img_tk

# GUI oluştur
root = tk.Tk()
root.title("YOLOv8 Tahmin GUI")
root.geometry("450x500")

btn = tk.Button(root, text="Resim Seç ve Tahmin Yap", command=open_image)
btn.pack(pady=20)

panel = tk.Label(root)
panel.pack()

root.mainloop()