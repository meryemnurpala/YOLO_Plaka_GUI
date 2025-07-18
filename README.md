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
> Not: Büyük veri/model dosyalarını yüklemeyin. Sadece kod ve arayüz dosyalarını ekleyin.

---

## 1. Terminali Aç ve plate-project Klasörüne Gir

```sh
cd "C:\\Users\\benme\\Desktop\\gyk ödevli kodlar\\gyk-computer-vision-master\\plate-project"
```

---

## 2. (Varsa) Eski Git Geçmişini Temizle

```sh
rmdir /s /q .git
```

---

## 3. Yeni Git Repo Başlat

```sh
git init
```

---

## 4. Uzak Repo Ekle

```sh
git remote add origin https://github.com/meryemnurpala/Yolo_Interface_Plaka.git
```

---

## 5. Sadece Gerekli Dosyaları Ekle

```sh
git add app.py templates static README.md
```

---

## 6. Commit Yap

```sh
git commit -m "YOLO Plaka Tanıma Web Arayüzü ve Türkçe README"
```

---

## 7. Ana Branch’i Ayarla

```sh
git branch -M main
```

---

## 8. GitHub’a Yükle (Zorla, ilk yükleme için)

```sh
git push -f origin main
```

---

### **Notlar:**
- Eğer `requirements.txt` dosyan yoksa, Flask ve Ultralytics gibi temel gereksinimleri eklemen iyi olur.
- Eğer `git` komutlarında hata alırsan, hatayı bana ilet, hemen çözüm bulayım.
- Yükleme sonrası GitHub’da sadece şunlar olacak:  
  - `app.py`, `templates/`, `static/`, `README.md`

---

**Yukarıdaki adımları uygularsan kesin olarak yüklenir. Hala sorun yaşarsan, aldığın hata mesajını bana ilet, adım adım birlikte çözelim!**