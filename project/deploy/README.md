
# 🛰️ Binárna klasifikácia snímok s meteormi

Projekt poskytuje kontajnerizovaný systém na klasifikáciu snímok s meteormi z AMOS kamier pomocou predtrénovaného modelu strojového učenia. Proces klasifikácie je zabalený v Python skripte (`process_images.py`) a je spúšťaný v izolovanom prostredí pomocou Dockeru.

---

## 🧰 Prerekvizity

Pre úspešné spustenie klasifikácie je potrebné:

- **Operačný systém**: Windows 10 alebo novší  
- **Docker Desktop**: Nainštalovaný a spustený ( → [Stiahnuť Docker](https://www.docker.com/products/docker-desktop) )
- **Projektový adresár** (napr. `TUKE_AMOS`) obsahujúci:
  - `Dockerfile`
  - `process_images.py` – skript, ktorý spúšťa klasifikáciu
  - modely natrénované na binárnu klasifikáciu snímok:
    - `convnext_model_legacy.pth`
    - `yolov11_model.pt`
    → uložené v adresári `./models/`
  - adresár `./results/`, do ktorého budú uložené výstupy klasifikácie
- **Zložku s obrázkami**: napr. `images/AMOS_DATA_20250408` – snímky určené na klasifikáciu

---

## 🚀 Návod na spustenie

### 📁 Krok 1: Otvorenie príkazového riadku

Na klávesnici stlač **Win + S**, zadaj `cmd` alebo `PowerShell`, alebo klikni na **Štart**, napíš `cmd` alebo `PowerShell` a otvor konzolu.

---

### 📂 Krok 2: Prejdenie do adresára s projektom

Nastaví sa aktuálny adresár na ten, v ktorom sa nachádzajú súbory `Dockerfile` a `process_images.py`.

```bash
cd C:\Users\ago\Desktop\TUKE_AMOS
```

---

### ⚙️ Krok 3: Vytvorenie Docker image

Vytvorí sa spustiteľný balík (Docker image), ktorý obsahuje všetko potrebné na klasifikáciu – vrátane kódu, knižníc a modelov.

```bash
docker build -t meteordetection .
```

**Vysvetlenie:**
- `docker build` spustí proces zostavovania image
- `-t meteordetection` priradí vytvorenému image názov `meteordetection`
- `.` znamená, že Docker použije aktuálny adresár ako kontext (musí obsahovať `Dockerfile`)

---

### ▶️ Krok 4: Spustenie klasifikácie snímok

```bash
docker run --rm -v "C:/Users/ago/Desktop/TUKE_AMOS:/app" --entrypoint python meteordetection process_images.py --original_input_dir "C:/Users/ago/Desktop/TUKE_AMOS/images/AMOS_DATA_20250408"
```

**Vysvetlenie:**
- `docker run` spustí nový kontajner
- `--rm` zabezpečí, že po ukončení sa kontajner automaticky odstráni
- `-v "C:/Users/ago/Desktop/TUKE_AMOS:/app"` pripojí lokálny adresár do kontajnera (bude vo vnútri kontajnera dostupný ako `/app`)
- `--entrypoint python` prepíše predvolený príkaz kontajnera a spustí Python
- `meteordetection` je názov vytvoreného Docker image
- `process_images.py` je skript, ktorý sa spustí
- `--original_input_dir` určuje priečinok s obrázkami na klasifikáciu

---

## 📄 Výstup

Výstup klasifikácie sa uloží do adresára `./results/` vo forme textového súboru s názvom:

```
vysledky_<časová_pečiatka>.txt
```

### 📌 Formát výstupu:

Každý riadok výstupného súboru má nasledovnú štruktúru:

```
<absolútna_cesta_k_obrázku> <pravdepodobnosť> <klasifikácia>
```

#### Príklad:
```
C:/Users/ago/Desktop/TUKE_AMOS/images/AMOS_DATA_20250408/M20240807_200500_AGO-ALLSKY_P.jpg 0.12 Nemet
```

#### Popis:

| Pole | Význam |
|------|--------|
| **Cesta k obrázku** | Úplná lokálna cesta k `.jpg` súboru |
| **Pravdepodobnosť** | Číslo medzi 0 a 1 – vyjadruje, na koľko percent si je model istý, že sa na snímke nachádza meteor |
| **Klasifikácia** | Výsledná trieda podľa modelu: <br>• `Met` – meteor sa nachádza na snímke <br>• `Nemet` – meteor sa na snímke nenachádza |

---

## ℹ️ Poznámka

Táto dokumentácia vznikla ako súčasť diplomovej práce realizovanej na Katedre kybernetiky a umelej inteligencie na Technickej univerzite v Košiciach.

---
