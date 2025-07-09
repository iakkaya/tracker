# Object Detection and Tracking Project

Bu proje, OpenCV ve Python kullanarak nesne tespiti ve takibi gerçekleştiren bir uygulamadır. Proje, çeşitli makine öğrenmesi modelleri kullanarak video akışlarında nesneleri tespit etmek ve izlemek için geliştirilmiştir.

## 🚀 Özellikler

- **Gerçek zamanlı nesne tespiti**
- **Çoklu nesne takibi**
- **Çeşitli detection modelleri desteği (YOLO, SSD, MobileNet)**
- **Webcam ve video dosyası desteği**
- **Bounding box görselleştirme**
- **Performance metrikleri**

## 📋 Gereksinimler

### Sistem Gereksinimleri
- Python 3.7+
- OpenCV 4.x
- PyCharm IDE (önerilen)

### Bağımlılıklar
```bash
pip install -r requirements.txt
```

## 🛠️ Kurulum

1. **Repoyu klonlayın:**
```bash
git clone https://github.com/yourusername/object-detection-tracker.git
cd object-detection-tracker
```

2. **Sanal ortam oluşturun:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows
```

3. **Bağımlılıkları yükleyin:**
```bash
pip install -r requirements.txt
```

4. **Modelleri indirin:**
```bash
python download_models.py
```

## 📁 Proje Yapısı

```
object-detection-tracker/
├── src/
│   ├── detection/
│   │   ├── __init__.py
│   │   ├── yolo_detector.py
│   │   ├── ssd_detector.py
│   │   └── base_detector.py
│   ├── tracking/
│   │   ├── __init__.py
│   │   ├── kalman_tracker.py
│   │   ├── centroid_tracker.py
│   │   └── base_tracker.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── video_utils.py
│   │   ├── drawing_utils.py
│   │   └── config_loader.py
│   └── main.py
├── models/
│   ├── yolo/
│   ├── ssd/
│   └── mobilenet/
├── data/
│   ├── videos/
│   ├── images/
│   └── annotations/
├── configs/
│   ├── yolo_config.yaml
│   ├── ssd_config.yaml
│   └── default_config.yaml
├── tests/
│   ├── test_detection.py
│   ├── test_tracking.py
│   └── test_utils.py
├── docs/
│   ├── API.md
│   ├── MODELS.md
│   └── TUTORIAL.md
├── requirements.txt
├── setup.py
├── download_models.py
├── .gitignore
├── LICENSE
└── README.md
```

## 🎯 Kullanım

### Temel Kullanım
```bash
python src/main.py --input video.mp4 --model yolo --output results.avi
```

### Webcam ile Kullanım
```bash
python src/main.py --input webcam --model yolo
```

### Parametreler
- `--input`: Girdi kaynağı (video dosyası, webcam veya görüntü)
- `--model`: Kullanılacak model (yolo, ssd, mobilenet)
- `--output`: Çıktı dosyası (isteğe bağlı)
- `--confidence`: Güven eşiği (varsayılan: 0.5)
- `--nms-threshold`: NMS eşiği (varsayılan: 0.4)

## 🧠 Desteklenen Modeller

### YOLO (You Only Look Once)
- YOLOv3, YOLOv4, YOLOv5 desteği
- Hızlı ve doğru tespit
- Gerçek zamanlı uygulamalar için ideal

### SSD (Single Shot MultiBox Detector)
- MobileNet-SSD
- Hafif ve mobil cihazlar için optimize
- Hızlı inference

### MobileNet
- Hafif ve verimli
- Mobil ve embedded sistemler için

## 📊 Performance

| Model | FPS | mAP | Boyut |
|-------|-----|-----|-------|
| YOLOv5 | 45 | 0.65 | 14MB |
| SSD-MobileNet | 60 | 0.55 | 27MB |
| YOLOv4 | 30 | 0.70 | 250MB |

## 🔧 Konfigürasyon

Proje konfigürasyonları `configs/` klasöründe YAML dosyaları olarak saklanır:

```yaml
# yolo_config.yaml
model:
  type: "yolo"
  weights: "models/yolo/yolov5s.pt"
  confidence: 0.5
  nms_threshold: 0.4
  
classes:
  - "person"
  - "car"
  - "bicycle"
  - "drone"
  
tracking:
  max_disappeared: 10
  max_distance: 100
```

## 📚 Dokümantasyon

Detaylı dokümantasyon için:
- [API Referansı](docs/API.md)
- [Model Dokümantasyonu](docs/MODELS.md)
- [Tutorial](docs/TUTORIAL.md)

## 🧪 Test Etme

```bash
# Tüm testleri çalıştır
python -m pytest tests/

# Belirli test dosyasını çalıştır
python -m pytest tests/test_detection.py

- [ismail](https://github.com/iakkaya) - Proje geliştiricisi

## 📧 İletişim

Sorularınız için:
- Email: iss.akkaya@hotmail.com 
- GitHub:iakkaya



