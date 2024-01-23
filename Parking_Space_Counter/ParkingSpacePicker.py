import cv2
import pickle # nesneleri dosyaya yazmak ve dosyadan okumak için kullanılan bir kütüphanedir.

width, height = 107,48

try:
    with open("CarParkPos","rb") as f:
        posList = pickle.load(f)
except: 
    posList=[] # try kısmında belirttiğimiz dosyada içerik bulamazsa boş bir liste üretir


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN: #sol tıklama ile yeni park alanı ekler
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN: # sağ tıklama ile mevcut park alanını kaldırır
        for i, pos in enumerate(posList):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)
    
    with open("CarParkPos", "wb") as f:
        pickle.dump(posList,f) # yaptığımız değişiklikleri CarParkPos'a kaydeder.


while True:
    img= cv2.imread("carParkImg.png")
    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+width, pos[1]+height),(255,0,255),2)

        cv2.imshow("Image",img)
        cv2.setMouseCallback("Image", mouseClick)
    if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cv2.destroyAllWindows()