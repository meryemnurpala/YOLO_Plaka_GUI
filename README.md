# YOLOv8 Plaka Tespit GUI

Bu proje, YOLOv8 modeli kullanarak görsel üzerinde plaka tespiti yapan basit bir Python ve Tkinter tabanlı grafik arayüz uygulamasıdır. Kullanıcı, bir görsel seçip model ile tespit işlemini gerçekleştirebilir ve sonucu arayüzde görebilir.

## Özellikler
- Eğitilmiş YOLOv8 modeli ile görsel üzerinde tespit
- Basit ve kullanıcı dostu grafik arayüz (Tkinter)
- Görsel seçip sonucu anında görüntüleme

## Gereksinimler
- Python 3.8+
- [Ultralytics YOLO](https://docs.ultralytics.com/) (`ultralytics`)
- OpenCV (`opencv-python`)
- Pillow (`Pillow`)

Gereksinimleri yüklemek için:
```bash
pip install ultralytics opencv-python Pillow
```

## Kullanım
1. Eğitilmiş YOLOv8 model ağırlık dosyanızın `runs/detect/train2/weights/best.pt` konumunda olduğundan emin olun veya `main.py` dosyasındaki yolu güncelleyin.
2. Uygulamayı başlatmak için:
```bash
python main.py
```
3. Açılan pencerede "Resim Seç ve Tahmin Yap" butonuna tıklayın, bir görsel seçin ve sonucu görün.

## Dosya Yapısı
- `main.py` - Ana uygulama dosyası (GUI ve tahmin fonksiyonları)
- `data.yaml` - Veri kümesi ayar dosyası (sadece eğitim için gerekli)
- `yolov8n.pt` - (Opsiyonel) Temel YOLOv8 modeli
- `runs/detect/train2/weights/best.pt` - Eğitilmiş model ağırlıkları

## Notlar
- Bu arayüz eğitim ve demo amaçlıdır.
- Kendi modelinizi eğitip, ağırlık dosyasının yolunu kodda güncelleyerek kullanabilirsiniz.

---

**Hazırlayan:** Meryemnur Pala