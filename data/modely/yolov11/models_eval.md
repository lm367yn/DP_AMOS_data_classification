## Dataset details

| Kategória objektu            | Počet obrázkov |
|------------------------------|----------------|
| Búrky                        | 202            |
| Lietadlá                     | 229            |
| Oblaky                       | 21             |
| Satelity - blikajúce         | 78             |
| Satelity - dlhé              | 25             |
| Satelity - krátke            | 57             |
| Sprites                      | 429            |
| Svetlá horizont              | 723            |
| Vtáky, netopiere, hmyz       | 218            |
| Rôzne                        | 379            |
| **Celkom Nemeteory**         | **2434**       |
| Meteory                      | 6309           |



**Train, Valid, Test Split**

| Set          | Imgs w Meteor | Imgs Non-Meteor |     All          |
| :----------- | :-----------: | :-------------: | -----------:     | 
| Train        |   4 130       | 1400            | 5 530 (77%)      |
| Valid        |   813         | 186             | 999  (14%)       |
| Test         |   599         | 47              | 646  (9%)        |
|              |   5 542       | 1 633           | 7 175            |


## Models
### 1.) :milky_way: Custom CNN

- task: binary classification

- stavba:
![image](https://github.com/user-attachments/assets/68802c75-cd73-4e36-a1d0-455c631ccb52)

**Training**

![image](https://github.com/user-attachments/assets/be8bdf66-5d62-4320-9e5d-a974e9aaa57d)


**Evaluation**



### 2.) :milky_way: yolov11

- task: object detection (0 - Meteor)

**Training**
- Preprocessing steps: Resize (Stretch to 1280x960); Grayscaled
- Augmentations: Outputs per training example: 3 (Flip: Horizontal, Vertical; Rotation: Between -20° and +20°)
  
![image](https://github.com/user-attachments/assets/28762d2b-dd6c-4899-9fc6-a73e83743b95)

![image](https://github.com/user-attachments/assets/a9b0b386-48e1-4861-b255-f8cde316394e)



**Evaluation**
- threshold: confid > 0.31

| Ground Truth/Prediction | Meteors   | Non-Meteors   |
|--------------------|-------------|-------------|
| Meteors            | TP = 580    | FN = 19     |
| Non Meteors        | FP = 24     | TN = 23     |

- results: TP : 580/599 , TN : 23/47
- Precision = TP / (TP + FP) = 0.9603
- Recall = TP / (TP + FN) = 0.9683
- F1 Score = 2 . (P . R) / (P + R) = 0.9643


### 3.) :milky_way: Vision Transformer (ViT)

- task: binary classification

**Training**
- Preprocessing steps: Resize (Stretch to 1280x960)
- Augmentations: Outputs per training example: 3 (Flip: Horizontal, Vertical; Rotation: Between -18° and +18°)

![image](https://github.com/user-attachments/assets/22ee9367-3d70-4867-a01e-549c3daf559a)

**Evaluation**

- threshold: confid > 0.5

| Ground Truth/Prediction | Meteors   | Non-Meteors   |
|--------------------|-------------|-------------|
| Meteors            | TP = 471    | FN = 128     |
| Non Meteors        | FP = 22     | TN = 25     |

- results: TP : 471/599 , TN : 25/47
- Precision = TP / (TP + FP) = 0.9553
- Recall = TP / (TP + FN) = 0.7863
- F1 Score = 2 . (P . R) / (P + R) = 0.8626

### 4.) :milky_way: ResNet50

- task: binary classification

**Training**
- Preprocessing steps: Resize (Stretch to 1280x960); Grayscale: Applied
- Augmentations: Outputs per training example: 4 (Flip: Horizontal, Vertical; Rotation: Between -18° and +18°)

![image](https://github.com/user-attachments/assets/bc15400f-86c1-4251-9b1b-5a8dcf42f158)

**Evaluation**

- threshold: confid > 0.5

| Ground Truth/Prediction | Meteors   | Non-Meteors   |
|--------------------|-------------|-------------|
| Meteors            | TP = 273    | FN = 326     |
| Non Meteors        | FP = 8     | TN = 39     |

- results: TP : 273/599 , TN : 39/47
- Precision = TP / (TP + FP) = 0.9681
- Recall = TP / (TP + FN) = 0.4558
- F1 Score = 2 . (P . R) / (P + R) = 0.6198

### 5.) :milky_way: ResNet101

- task: binary classification

**Training**
- Preprocessing steps: Resize (Stretch to 1280x960); Auto-Adjust Contrast; Grayscale: Applied
- Augmentations: Outputs per training example: 4 (Flip: Horizontal, Vertical; Rotation: Between -18° and +18°)

![image](https://github.com/user-attachments/assets/63d69e21-be75-434d-b41c-a945d7de56c4)

**Evaluation**

- threshold: confid > 0.5

| Ground Truth/Prediction | Meteors   | Non-Meteors   |
|--------------------|-------------|-------------|
| Meteors            | TP = 202    | FN = 397     |
| Non Meteors        | FP = 9     | TN = 38     |

- results: TP : 202/599 , TN : 38/47
- Precision = TP / (TP + FP) = 0.9573
- Recall = TP / (TP + FN) = 0.3372
- F1 Score = 2 . (P . R) / (P + R) = 0.4987
 
### 5.) :milky_way: convnext_small

- task: binary classification
