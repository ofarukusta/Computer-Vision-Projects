import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

################################
wCam, hCam = 640, 480
################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector()

devices = AudioUtilities.GetSpeakers() # Bilgisayardaki hoparlörü devices olarak tanıtıyoruz.
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None) # Hoparlörün ses düzeyini kontrol etmek için gerekli arayüzü oluşturur.
volume = cast(interface, POINTER(IAudioEndpointVolume)) # Ses düzeyini volume adlı değişkene atıyoruz.

volRange = volume.GetVolumeRange() # Ses düzeyinin min ve max değerlerini alır aşağıda 0 ve 1 olarak değer verdik
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0
area = 0
colorVol = (255, 0, 0)

while True:
    success, img = cap.read()

    
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=True)
    if len(lmList) != 0:

        # Filter based on size
        area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100
        # print(area)
        if 250 < area < 1000:

            # Find Distance between index and Thumb
            length, img, lineInfo = detector.findDistance(4, 8, img) # Baş parmak ve İşaret Parmağı arasındaki mesafeyi hesapla
            # print(length)

            # Convert Volume
            volBar = np.interp(length, [50, 200], [400, 150]) # Ses Çubuğu anlık olarak güncellenir.
            volPer = np.interp(length, [50, 200], [0, 100]) # Ses Düzeyi anlık olarak güncellenir.

            # Reduce Resolution to make it smoother
            smoothness = 10
            volPer = smoothness * round(volPer / smoothness)

            # Check fingers up
            fingers = detector.fingersUp()
            # print(fingers)

            # If pinky is down set volume
            if not fingers[4]:
                volume.SetMasterVolumeLevelScalar(volPer / 100, None)
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                colorVol = (0, 255, 0)
            else:
                colorVol = (255, 0, 0)

    # Drawings
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)
    cVol = int(volume.GetMasterVolumeLevelScalar() * 100) # Mevcut ses düzeyini alır.
    cv2.putText(img, f'Vol Set: {int(cVol)}', (400, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, colorVol, 3)

    # Frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime) # FPS'i anlık olarak hesapladığımız kısım.
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)

    cv2.imshow("Img", img)

    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break 


# Kodu çalıştırdıktan sonra baş ve işaret parmağı aralıklı tutup diğer parmakları kaparsanız, kod, optimum düzeyde çalışacaktır.