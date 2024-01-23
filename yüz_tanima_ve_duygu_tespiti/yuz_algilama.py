from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt


img_path = "deneme1.jpg"
img= cv2.imread(img_path)

plt.imshow(img)
plt.show()

analiz = DeepFace.analyze(img_path , 
        actions = ['age', 'gender'])

print(analiz)

