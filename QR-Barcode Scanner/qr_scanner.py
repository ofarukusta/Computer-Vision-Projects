import cv2
from  pyzbar.pyzbar import decode
import time

cap = cv2.VideoCapture(0)
cap.set(5, 640)
cap.set(6, 480)

camera= True
while camera:
    success, frame = cap.read()

    barcodes = decode(frame)
    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        cv2.putText(frame,f"Barcode Type:{barcodeType}, Barcode Data: {barcodeData}",(10,50),1,1,(255,0,0),2,cv2.FONT_HERSHEY_TRIPLEX) # Barkodda okunan yazının ekranda gösterilmesi
        print(f"Barcode Type: {barcodeType}") # Barkodda tipinin çıktı olarak verilmesi
        print(f"Barcode Data: {barcodeData}") # Barkodda okunan yazının çıktı olarak verilmesi
        
        
# Points ile başlayıp if yapısı ile devam eden kısım opsiyoneldir. Kod okuma işlemi buraya kadar yapılan kısımda gerçekleştirilmiştir. Kalan kısımda, taranan barkod dikdörtgen içine alınarak gösterilecektir.
        points = barcode.polygon
        if points:
            rectPts = [tuple(point) for point in points] # Köşegenler için noktaları çekiyoruz
            
            # Barkodun sol üst ve sağ alt köşe noktalarını bulma
            left_top = min(rectPts, key=lambda x: x[0] + x[1]) # Sol üst köşe noktası
            right_bottom = max(rectPts, key=lambda x: x[0] + x[1]) # Sağ alt köşe noktası
            cv2.rectangle(frame,left_top,right_bottom,(0,0,255),2) # Barkodu dikdörtgene aldırıyoruz.
        


    cv2.imshow("qr_Scanner", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):  # q tuşu ile koddan çıkıyoruz
        break

cv2.destroyAllWindows()
cap.release()

