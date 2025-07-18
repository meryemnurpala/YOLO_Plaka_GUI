# YOLO Plaka Tanıma Web Arayüzü

Bu proje, YOLOv8 tabanlı araç plaka tanıma için modern ve kullanıcı dostu bir web arayüzü sunar.

## Özellikler
- Flask tabanlı web sunucu
- Modern ve responsive arayüz (TailwindCSS, FontAwesome, Poppins)
- İstanbul arka planı ve karanlık mod desteği
- Plaka tespiti sonrası görsel karşılaştırma
- Toplam tespit sayacı

## Kullanım
1. Gerekli Python paketlerini yükleyin:
   ```
   pip install -r requirements.txt
   ```
2. Flask sunucusunu başlatın:
   ```
   python app.py
   ```
3. Tarayıcıda `http://localhost:5000` adresine gidin.

## Klasörler ve Dosyalar
- `app.py` : Ana Flask uygulaması
- `templates/` : HTML şablonları (index, result, about)
- `static/style.css` : (Varsa) ek stil dosyası
- `static/istanbul.jpg` : Arka plan görseli
- `static/uploads/` ve `static/results/` : Yüklenen ve tahmin edilen görseller (boş bırakılabilir)
- `runs/detect/train2/weights/best.pt` : (Varsa) YOLO model dosyası

## Geliştirici
**meryemnur pala**

---

<img width="1862" height="979" alt="Ekran görüntüsü 2025-07-18 211745" src="https://github.com/user-attachments/assets/82db8930-d26a-4edb-b541-102f09e6f070" />
<img width="1838" height="983" alt="Ekran görüntüsü 2025-07-18 211800" src="https://github.com/user-attachments/assets/fb8bdb8b-f406-44bd-ad7f-eb7a610c74ce" />
