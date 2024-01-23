from keras.preprocessing.image import img_to_array
import imutils
import cv2
from keras.models import load_model
import numpy as np
import h5py 

##############################################################################################

"""
Yuz algilayici olarak yuklenecek olan dosyanin ve duygu siniflandirici modelin yolu belirtilir
"""

detection_model_path = 'haarcascade_files/haarcascade_frontalface_default.xml' # detection icin haarcascade'i cagiriyoruz #
model_path = 'models/deneme.hdf5' # egitim yapildiktan sonra olusan agirlik dosyalarini buraya girebilirsiniz #
emotion_model_path = h5py.File(model_path,'r')

##############################################################################################

##############################################################################################
"""
Modelleri sisteme yukleyip, duygu siniflarini olusturuyoruz
"""

face_detection = cv2.CascadeClassifier(detection_model_path)  # yuz algilayici modeli haar cascade ile yukleyecegiz #
emotion_classifier = load_model(emotion_model_path, compile=False)  # duygu tanimlayici modeli yukarida tanittigmiz yoldan cekiyoruz #
EMOTIONS = ["angry(kizgin)", "disgust(igrenmis)", "scared(korkmus)", "happy(mutlu)", "sad(uzgun)", "surprised(saskin)", "neutral(dogal)"]

# Duygu durumlarini listeledik #
##############################################################################################

cv2.namedWindow('yuz_tarama')
camera = cv2.VideoCapture(0)
while True:
    frame = camera.read()[1] # kameradan 1 frame okunur # 
    #reading the frame
    frame = imutils.resize(frame,width=300) # Goruntuyu 300 genisliginde boyutlandirdir #
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # frameler gray turune donusturulur, yuz algilama islemi bu sekilde yapilacak #
    faces = face_detection.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE) # Haar Cascade ile yuz tespit algoritmasini calistiriyoruz #
    
    canvas = np.zeros((250, 300, 3), dtype="uint8")
    frameClone = frame.copy()
    if len(faces) > 0: # Ekranda yuz algilanmasi durumunda Region Of Interest(ROI) calisarak tespit edilen yuzu islem yapmak icin ele alir #
        faces = sorted(faces, reverse=True,
        key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
        (fX, fY, fW, fH) = faces
                    
        roi = gray[fY:fY + fH, fX:fX + fW]
        roi = cv2.resize(roi, (48, 48))
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)
        # ROİ ile yüzü algılayarak hedef alan olarak seçiyoyruz
        
        preds = emotion_classifier.predict(roi)[0] # ROI'de secilen yuz, duygu siniflandirma algoritmasina tabii tutulur #
        emotion_probability = np.max(preds)
        label = EMOTIONS[preds.argmax()] # En yuksek olasiliga sahip duygu durumu label olarak alinir #
    else: continue # Yuz tespit edilmezse devam edilir #

 
    for (i, (emotion, prob)) in enumerate(zip(EMOTIONS, preds)): # her bir duygu durumu ele alinir #
                
                text = "{}: {:.2f}%".format(emotion, prob * 100) # tum duygu durumlari yuzde olarak ele alinir, ekrana da yazdiracagiz #
 
                

                
                w = int(prob * 300)
                cv2.rectangle(canvas, (7, (i * 35) + 5),
                (w, (i * 35) + 35), (0, 0, 255), -1)
                cv2.putText(canvas, text, (10, (i * 35) + 23),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45,
                (255, 255, 255), 2)
                cv2.putText(frameClone, label, (fX, fY - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),
                              (0, 0, 255), 2)

    cv2.imshow('Yuz_Tarama', frameClone)
    cv2.imshow("Duygu_Analizi", canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
#    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
#    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
