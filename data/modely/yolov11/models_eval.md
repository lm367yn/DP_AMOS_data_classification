## Dataset details
![image](https://github.com/user-attachments/assets/075e4ea0-7ac6-48ff-82ed-fe702faba88b)

## Models
### :new_moon: yolov11

- task: object detection (0 - Meteor)

**Training**
- Preprocessing steps: Resize (Stretch to 1280x960); Grayscaled
- Augmentations: Outputs per training example: 3 (Flip: Horizontal, Vertical; Rotation: Between -20° and +20°)
![image](https://github.com/user-attachments/assets/28762d2b-dd6c-4899-9fc6-a73e83743b95)
- 


**Evaluation**
- threshold: conf > 0.31
- results: TP : 580/599 , TN : 23/47

### :first_quarter_moon: Vision Transformer (ViT)

- task: binary classification

**Training**
- Preprocessing steps: Resize (Stretch to 1280x960)
- Augmentations: Outputs per training example: 3 (Flip: Horizontal, Vertical)

![image](https://github.com/user-attachments/assets/123055a7-2cc9-48ac-838f-5be9db96507e)

### :full_moon: ResNet

- task: binary classification

**Training**
- Preprocessing steps: Resize (Stretch to 1280x960)
- Augmentations: Outputs per training example: 3 (Flip: Horizontal, Vertical; Rotation: Between -18° and +18°)
