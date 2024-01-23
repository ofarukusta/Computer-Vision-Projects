<div align= "center">
<h1>Yüz Bölge Analizi</h1>
</div>

Mediapipe, çeşitli bilgisayar görüşü görevlerini kolaylaştıran bir kütüphanedir. Burada, yüz tespiti için kullanacağımız Mediapipe kütüphanesini içeriye almamız gerekiyor.

Sonrasında Mediapipe’ın iki fonksiyonunu kullanarak yüz algılama ve yüz içerisinden ağız, göz, burun, kulak algılama işlemlerini yaptırıyoruz:

```
•	(mp.solutions.face_detection.FaceDetection) : sınıfından bir nesne oluşturuyoruz. Bu nesne, yüz tespiti yapmak için kullanılacak.
```
```
•	(mp_drawing = mp.solutions.drawing_utils) : Yüz tespiti sonuçlarını görüntüye çizmek için kullanılacak yardımcı fonksiyonları içeren bir modülü içeriye alıyoruz.
```

OpenCV modülü ile kamerayı açtıktan sonra döngü içerisinde BGR görüntüyü RGB’ye çeviriyirouz. Mediapipe bu şekilde işlem yapacak. Sonrasında RGB görüntüyü yüz tespit modeline veriyoruz:
```
•	(results = mp_face_detection.process(frame) ) : Dönüştürülmüş kareyi yüz tespit modeline veriyoruz. Bu, yüz tespiti sonuçlarını döndürecektir.
```

Daha sonrasında tespit olması şartını koşarak yüzü kareleme işlemine tabii tutarak detection işlemini yapıyoruz:
```
•	if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(frame, detection)
```

<h3>Koolac'ın yaptığı benzer bir uygulama görseli</h3>


![image](https://github.com/ofarukusta/Computer-Vision-Projects/assets/110857814/8faa2447-5714-48f7-9337-7bcb7f9bd25b)
