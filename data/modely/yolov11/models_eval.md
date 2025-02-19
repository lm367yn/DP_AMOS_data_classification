## Dataset details

Raw:
| Set          | Imgs w Meteor | Imgs Non-Meteor |     All          |
| :----------- | :-----------: | :-------------: | -----------:     | 
| Train        |   4 129       | 1401            | 5 530 (77%)      |
| Valid        |   813         | 186             | 999  (14%)       |
| Test         |   599         | 47              | 646  (9%)        |
|              |   5 541       | 1 634           | 7 175            |

S augmentaciou trenovacky:
![image](https://github.com/user-attachments/assets/075e4ea0-7ac6-48ff-82ed-fe702faba88b)

## Models
### 1.) :milky_way: yolov11

- task: object detection (0 - Meteor)

**Training**
- Preprocessing steps: Resize (Stretch to 1280x960); Grayscaled
- Augmentations: Outputs per training example: 3 (Flip: Horizontal, Vertical; Rotation: Between -20° and +20°)
  
![image](https://github.com/user-attachments/assets/28762d2b-dd6c-4899-9fc6-a73e83743b95)

![image](https://github.com/user-attachments/assets/a9b0b386-48e1-4861-b255-f8cde316394e)



**Evaluation**
- threshold: conf > 0.31
- results: TP : 580/599 , TN : 23/47



### 2.) :milky_way: Vision Transformer (ViT)

- task: binary classification

**Training**
- Preprocessing steps: Resize (Stretch to 1280x960)
- Augmentations: Outputs per training example: 3 (Flip: Horizontal, Vertical)

![image](https://github.com/user-attachments/assets/123055a7-2cc9-48ac-838f-5be9db96507e)

**Evaluation**
![image](https://github.com/user-attachments/assets/e2e507ba-a921-4fd7-a7eb-a969fd59084d)



### 3.) :milky_way: ResNet101

- task: binary classification

**Training**
- Preprocessing steps: Resize (Stretch to 1280x960)
- Augmentations: Outputs per training example: 3 (Flip: Horizontal, Vertical; Rotation: Between -18° and +18°)

![image](https://github.com/user-attachments/assets/22ee9367-3d70-4867-a01e-549c3daf559a)

**Evaluation**

![image](https://github.com/user-attachments/assets/7e757e66-931d-437d-b180-8bb73ea701e6)

  
