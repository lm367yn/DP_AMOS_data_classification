import os
import torch
from datetime import datetime
from ultralytics import YOLO

# === CESTY ===
model_path = "/app/models/yolov11_model.pt"
image_dir = "/app/images"
original_input_dir = r"C:\Users\ago\Desktop\TUKE_AMOS\images"
output_dir = "/app/results"
threshold = 0.0
device = torch.device("cpu")

# === Výstupný názov súboru ===
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_path = os.path.join(output_dir, f"results_yolo_{timestamp}.txt")

# === Načítanie YOLO modelu ===
model = YOLO(model_path).to(device)
model.eval()

def predict_yolo(image_path, model, threshold=0.0):
    with torch.no_grad():
        results = model(image_path, verbose=False)
        detections = results[0].boxes
    confidences = [det[4] for det in detections.data.cpu().numpy() if det[4] > threshold]
    return max(confidences) if confidences else 0.0

# === Predikcia obrázkov ===
results = []
for fname in sorted(f for f in os.listdir(image_dir) if f.lower().endswith(".jpg")):
    img_path = os.path.join(image_dir, fname)
    prob = predict_yolo(img_path, model, threshold)
    label = "Met" if prob >= 0.5 else "Nemet"
    original_path = os.path.join(original_input_dir, fname).replace("/", "\\")
    results.append(f"{original_path} {prob:.2f} {label}\n")

# === Uloženie výsledkov ===
with open(output_path, "w") as f:
    f.writelines(results)

print(f"✅ YOLOv11 výsledky uložené do {output_path}")
