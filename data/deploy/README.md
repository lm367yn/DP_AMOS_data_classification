## Spustenie Dockeru v termináli s CNN modelom na detekciu meteorov

### cd C:\Users\ago\Desktop\TUKE_AMOS  
Tento príkaz nastaví aktuálny pracovný adresár v termináli na priečinok **TUKE_AMOS**, kde sa nachádzajú všetky potrebné súbory vrátane **Dockerfile, python skriptu a modelu**. Všetky nasledujúce príkazy sa vykonajú v tomto adresári.

### docker build -t meteordetection .  
Tento príkaz vytvorí Docker image s názvom **meteordetection** na základe **Dockerfile**, ktorý sa nachádza v aktuálnom priečinku (`.` znamená aktuálny adresár). Počas procesu sa nainštalujú všetky potrebné knižnice a závislosti, čím sa zabezpečí konzistentné prostredie pre beh modelu.

### docker run --rm -v "C:\Users\ago\Desktop\TUKE_AMOS\images:/app/images" -v "C:\Users\ago\Desktop\TUKE_AMOS\results:/app/results" meteordetection /app/images --output /app/results/results.txt  

Tento príkaz spustí kontajner vytvorený z Docker image **meteordetection** a vykoná detekciu meteorov na obrázkoch uložených v priečinku **images**.

- **`--rm`**: Po skončení procesu automaticky odstráni kontajner, čím sa zabráni zbytočnému hromadeniu dočasných kontajnerov.
- **`-v "C:\Users\ago\Desktop\TUKE_AMOS\images:/app/images"`**: Prepojí lokálny priečinok **images** s adresárom **/app/images** v kontajneri, aby model mohol načítať vstupné obrázky.
- **`-v "C:\Users\ago\Desktop\TUKE_AMOS\results:/app/results"`**: Prepojí lokálny priečinok **results** s adresárom **/app/results** v kontajneri, kam sa uložia výstupné výsledky.
- **`meteordetection`**: Označuje, ktorý Docker image sa použije na spustenie kontajnera.
- **`/app/images`**: Predáva skriptu cestu k obrázkom, ktoré sa majú analyzovať.
- **`--output /app/results/results.txt`**: Určuje, kam sa majú uložiť výsledky predikcie.

Po spustení tohto príkazu bude výsledný súbor **results.txt** obsahovať klasifikáciu obrázkov s označením **Met** (obsahuje meteor) alebo **Nemet** (neobsahuje meteor) a bude uložený v priečinku **results**.

