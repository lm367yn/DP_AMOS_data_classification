import os
import torch
import timm
import torch.nn as nn
from PIL import Image
from torchvision import transforms
from datetime import datetime

model_path = "/app/models/convnext_model_legacy.pth"
image_dir = "/app/images"
original_input_dir = r"C:\Users\ago\Desktop\TUKE_AMOS\images"
output_dir = "/app/results"
threshold = 0.5
device = torch.device("cpu")

transform = transforms.Compose([
    transforms.Resize((720, 720)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])

# Názov výstupného súboru
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_path = os.path.join(output_dir, f"results_{timestamp}.txt")

# Načítanie modelu
model = timm.create_model("convnext_small", pretrained=False, num_classes=1)
model.classifier = nn.Sequential(nn.Dropout(0.5), nn.Linear(model.num_features, 1))
with open(model_path, 'rb') as f:
    model.load_state_dict(torch.load(f, map_location=device))
model.eval()

# Predikcia a zápis do súboru
results = []
for fname in sorted(f for f in os.listdir(image_dir) if f.lower().endswith(".jpg")):
    img_path = os.path.join(image_dir, fname)
    img = transform(Image.open(img_path).convert('RGB')).unsqueeze(0)

    with torch.no_grad():
        prob = torch.sigmoid(model(img)).item()

    label = "Met" if prob >= threshold else "Nemet"
    # Pôvodná cesta na hostiteľskom systéme
    original_path = os.path.join(original_input_dir, fname).replace("/", "\\")
    results.append(f"{original_path} {prob:.2f} {label}\n")

# Uloženie do výsledného súboru
with open(output_path, "w") as f:
    f.writelines(results)

print(f"✅ Výsledky uložené do {output_path}")
