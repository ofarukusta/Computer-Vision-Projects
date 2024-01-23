import cvzone
import cv2
import mediapipe as mp 
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os


# Kamera'nın içe aktarılması ve boyut ayarlamaları #
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
 #Burada cv.resize kullanılmamasının sebebi, resize işlemi frameler üzerinden yapılır. capset kullaılmak istenilmezse, while döngüsü içinde kamera tanımının altına, frameler için resize uygulanabilir

# Segmentasyonu çalıştırıyoruz, Ekleyeceğimiz arka planı belirleyip, boyutu kendi ekran boyutumuzla aynı hale getiriyoruz. #
segmentor = SelfiSegmentation()
imgBg = cv2.imread("images/ofis1.jpg")
imgBg=cv2.resize(imgBg,(640,480))


while True:
    success, frame = cap.read()

    imgOut=segmentor.removeBG(frame,imgBg,cutThreshold=0.8)
    

    imgStacked=cvzone.stackImages([frame,imgOut],2,1)


    cv2.imshow("imgStacked",imgStacked)
    if cv2.waitKey(1) & 0xFF== ord("q"):
        break
