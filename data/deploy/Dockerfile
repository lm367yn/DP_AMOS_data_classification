FROM python:3.12-slim

# Inštalácia závislostí
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Aktualizácia pip a inštalácia rovnakých verzií knižníc ako v Datalabe
RUN pip install --upgrade pip

# Inštalácia CUDA-kompatibilných torch balíčkov z oficiálneho indexu
RUN pip install torch==2.6.0 torchvision==0.21.0

# Ostatné knižnice
RUN pip install timm==1.0.15 ultralytics==8.3.102 pillow==11.1.0 numpy==1.26.4

# Pracovný adresár
WORKDIR /app

# Skopírovanie kódu
COPY . /app/

# Spustenie skriptu
ENTRYPOINT ["python", "process_images.py"]
