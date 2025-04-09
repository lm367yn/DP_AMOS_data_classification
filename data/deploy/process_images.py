import os
import argparse
import torch
import timm
import torch.nn as nn
from PIL import Image
from torchvision import transforms
from ultralytics import YOLO
from datetime import datetime

# === Argumenty ===
parser = argparse.ArgumentParser()
parser.add_argument("--original_input_dir", required=True, help="Lokálna cesta k obrázkom")
args = parser.parse_args()

# === Dynamická cesta v kontajneri ===
original_input_dir = args.original_input_dir
subfolder = os.path.basename(original_input_dir)
image_root_dir = os.path.join("/app/images", subfolder)

# === Fixné cesty k modelom a výsledkom ===
convnext_path = "/app/models/convnext_model_legacy.pth"
yolov11_path = "/app/models/yolov11_model.pt"
output_dir = "/app/results"

device = torch.device("cpu")

# === Ensemble nastavenia ===
weights = {'convnexts': 0.5424, 'yolov11': 0.4576}
threshold = 0.441
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_path = os.path.join(output_dir, f"vysledky_{timestamp}.txt")

# === Transformácia ===
transform = transforms.Compose([
    transforms.Resize((720, 720)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])

# === Načítanie modelov ===
convnext_model = timm.create_model("convnext_small", pretrained=False, num_classes=1)
convnext_model.classifier = nn.Sequential(nn.Dropout(0.5), nn.Linear(convnext_model.num_features, 1))
with open(convnext_path, 'rb') as f:
    convnext_model.load_state_dict(torch.load(f, map_location=device))
convnext_model.eval()

yolo_model = YOLO(yolov11_path).to(device)
yolo_model.eval()

# === Predikcie ===
def predict_convnext(image_path):
    image = Image.open(image_path).convert('RGB')
    image_tensor = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        return torch.sigmoid(convnext_model(image_tensor)).item()

def predict_yolo(image_path, threshold=0.0):
    with torch.no_grad():
        results = yolo_model(image_path, verbose=False)
        detections = results[0].boxes
    confidences = [det[4] for det in detections.data.cpu().numpy() if det[4] > threshold]
    return max(confidences) if confidences else 0.0

# === Načítanie obrázkov ===
image_files = []
for root, _, files in os.walk(image_root_dir):
    for fname in files:
        if fname.lower().endswith(".jpg"):
            image_files.append(os.path.join(root, fname))

# === Vyhodnotenie a uloženie výsledkov ===
results = []
for img_path in sorted(image_files):
    pred_conv = predict_convnext(img_path)
    pred_yolo = predict_yolo(img_path)

    ensemble_prob = pred_conv * weights['convnexts'] + pred_yolo * weights['yolov11']
    label = "Met" if ensemble_prob >= threshold else "Nemet"

    rel_path = os.path.relpath(img_path, image_root_dir).replace("\\", "/")
    original_path = f"{original_input_dir}/{rel_path}"

    results.append(f"{original_path} {ensemble_prob:.2f} {label}\n")

with open(output_path, "w") as f:
    f.writelines(results)

print(f"Výsledky sú uložené do {output_path}")

