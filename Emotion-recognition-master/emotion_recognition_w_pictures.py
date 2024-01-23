import cv2
import h5py
import numpy as np
from keras_preprocessing.image import img_to_array
from keras.models import load_model
import matplotlib.pyplot as plt

########################################################################################################################################################
######## Analiz etmek istedigimiz görseli, kullanacagimiz agirlik dosyasini ve detection icin gerekli olan haarcascade paketlerini tanimliyoruz ########
image_path= "images/neutral.jpg"
model_path = "models/deneme.hdf5"
detection_model_path = "haarcascade_files/haarcascade_frontalface_default.xml"

########################################################################################################################################################
######## Duygu siniflandirma modeli ve yüz tanima modelini yükleyip, duygu etiketlerini tanimliyoruz. ########

emotion_model =  h5py.File(model_path,'r')
emotion_classifier = load_model(emotion_model, compile=False)
face_detection = cv2.CascadeClassifier(detection_model_path)
EMOTIONS = ["angry(kizgin)", "disgust(igrenmis)", "scared(korkmus)", "happy(mutlu)", "sad(uzgun)", "surprised(saskin)", "neutral(dogal)"]

########################################################################################################################################################
######## Fotograf uzerinden analiz gerceklestirecegimiz fonksiyonumuzu olusturuyoruz. ########

def duygu_analizi(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    for (fX,fY,fW,fH) in faces:
        roi = gray[fY:fY + fH, fX:fX + fW]
        roi = cv2.resize(roi, (48, 48))
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)

        preds = emotion_classifier.predict(roi)[0]
        emotion_probability = np.max(preds)
        label = EMOTIONS[preds.argmax()]

        print(f"En yüksek olasılık: {emotion_probability:.2f}")
        print(f"Tahmin edilen duygu: {label}")

        ######## İslemi tablolastirarak, tahmin sonuclarini grafige dökelim ########
        fig, ax = plt.subplots(1, 2, figsize=(10, 5))
        ax[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        ax[0].set_title('Resim')
        ax[0].axis('off')

        colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink'] # Rengi burada belirtiyoruz
        ax[1].barh(EMOTIONS, preds, color=colors)
        ax[1].set_title('Duygu Olasiliklari')
        
        for i, prob in enumerate(preds):
            ax[1].text(prob + 0.02, i, f'{prob*100:.2f}%', va='center', color='black', fontsize=10)
        plt.tight_layout()
        plt.show()
duygu_analizi(image_path)