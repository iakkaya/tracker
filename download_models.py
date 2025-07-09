#!/usr/bin/env python3
"""
Model indirme scripti
Proje için gerekli olan pre-trained modelleri indirir
"""

import os
import requests
import sys
from pathlib import Path
from tqdm import tqdm
from urllib.parse import urlparse

def download_file(url, destination):
    """Dosyayı progress bar ile indir"""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        
        with open(destination, 'wb') as file, tqdm(
            desc=os.path.basename(destination),
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
                    bar.update(len(chunk))
        
        print(f"✓ {destination} başarıyla indirildi")
        return True
    except Exception as e:
        print(f"✗ {destination} indirilemedi: {e}")
        return False

def create_directories():
    """Gerekli dizinleri oluştur"""
    directories = [
        "models/yolo",
        "models/ssd",
        "models/mobilenet",
        "data/videos",
        "data/images",
        "data/annotations",
        "results",
        "logs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"📁 {directory} dizini oluşturuldu")

def download_yolo_models():
    """YOLO modellerini indir"""
    print("\n🔥 YOLO modellerini indiriliyor...")
    
    yolo_models = {
        "yolov5s.pt": "https://github.com/ultralytics/yolov5/releases/download/v7.0/yolov5s.pt",
        "yolov5m.pt": "https://github.com/ultralytics/yolov5/releases/download/v7.0/yolov5m.pt",
        "yolov5l.pt": "https://github.com/ultralytics/yolov5/releases/download/v7.0/yolov5l.pt",
    }
    
    for model_name, url in yolo_models.items():
        destination = f"models/yolo/{model_name}"
        if not os.path.exists(destination):
            download_file(url, destination)
        else:
            print(f"⚠️  {model_name} zaten mevcut, atlaniyor")

def download_ssd_models():
    """SSD modellerini indir"""
    print("\n🚀 SSD modellerini indiriliyor...")
    
    ssd_models = {
        "ssd_mobilenet_v2_coco.pb": "http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz",
        "ssd_inception_v2_coco.pb": "http://download.tensorflow.org/models/object_detection/ssd_inception_v2_coco_2018_01_28.tar.gz",
    }
    
    # Not: Bu URL'ler tar.gz dosyalarını işaret eder, gerçek implementasyonda bunları extract etmek gerekir
    print("⚠️  SSD modelleri için manual indirme gerekli")
    print("   TensorFlow Model Zoo'dan indirip models/ssd/ klasörüne koyun")

def download_mobilenet_models():
    """MobileNet modellerini indir"""
    print("\n📱 MobileNet modellerini indiriliyor...")
    
    # MobileNet modelleri için placeholder
    print("⚠️  MobileNet modelleri için TensorFlow Hub kullanılacak")
    print("   Kod çalıştırıldığında otomatik olarak indirilecek")

def create_config_files():
    """Konfigürasyon dosyalarını oluştur"""
    print("\n⚙️  Konfigürasyon dosyaları oluşturuluyor...")
    
    # Default config
    default_config = """# Default Configuration
model:
  type: "yolo"
  confidence: 0.5
  nms_threshold: 0.4
  
input:
  source: "webcam"  # webcam, video file path, or image path
  
output:
  save_video: true
  save_path: "results/"
  show_fps: true
  
tracking:
  max_disappeared: 30
  max_distance: 50
  
visualization:
  show_labels: true
  show_confidence: true
  box_thickness: 2
  text_scale: 0.5
"""
    
    with open("configs/default_config.yaml", "w") as f:
        f.write(default_config)
    
    # YOLO config
    yolo_config = """# YOLO Configuration
model:
  type: "yolo"
  weights: "models/yolo/yolov5s.pt"
  confidence: 0.5
  nms_threshold: 0.4
  device: "auto"  # auto, cpu, cuda
  
classes:
  - "person"
  - "bicycle"
  - "car"
  - "motorcycle"
  - "airplane"
  - "bus"
  - "train"
  - "truck"
  - "boat"
  - "traffic light"
  
tracking:
  tracker_type: "kalman"
  max_disappeared: 30
  max_distance: 50
"""
    
    with open("configs/yolo_config.yaml", "w") as f:
        f.write(yolo_config)
    
    print("✓ Konfigürasyon dosyaları oluşturuldu")

def main():
    """Ana fonksiyon"""
    print("🚀 Object Detection & Tracking Projesi Setup")
    print("=" * 50)
    
    # Dizinleri oluştur
    create_directories()
    
    # Modelleri indir
    download_yolo_models()
    download_ssd_models()
    download_mobilenet_models()
    
    # Konfigürasyon dosyalarını oluştur
    create_config_files()
    
    print("\n" + "=" * 50)
    print("🎉 Setup tamamlandı!")
    print("\nSonraki adımlar:")
    print("1. requirements.txt dosyasını yükleyin: pip install -r requirements.txt")
    print("2. Kod dosyalarını src/ klasörüne ekleyin")
    print("3. python src/main.py --help ile kullanımı öğrenin")
    print("\n📖 Detaylı bilgi için README.md dosyasını okuyun")

if __name__ == "__main__":
    main()