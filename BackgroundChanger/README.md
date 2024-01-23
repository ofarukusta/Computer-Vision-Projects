<div align= "center">
<h1>Background Changer</h1>
</div>

Bu uygulamada Zoom'da olduğu gibi, arka plan değiştirme fonksiyonu geliştirilmiştir. Ekrandaki kişi görselden ayrıştırılarak başka bir alandaymış izlenimi verilmektedir.

![ornek](https://github.com/ofarukusta/Computer-Vision-Projects/assets/110857814/cb8d26c2-ca28-4186-8d62-23778bce8545)

Çeşitli arka planlar kod ile birlikte verilmiştir.

- <b>cvzone:</b> Bu kütüphane, çeşitli bilgisayarlı görüş görevlerini gerçekleştirmek için kullanılır.
- <b>mediapipe:</b> MediaPipe kütüphanesini içerir. Bu kütüphane, çeşitli medya işleme görevleri için kullanılır.
- <b>SelfiSegmentation:</b> cvzone kütüphanesinin içinde yer alan, selfie segmentasyonunu gerçekleştiren bir modülü içerir.
- <b>segmentor.removeBG(frame,imgBg,cutThreshold=0.8):</b> Selfie segmentasyonunu gerçekleştirir ve arka planı çıkarır. cutThreshold=0.8 parametresi, kesme eşiğini belirler.
- <b>cvzone.stackImages([frame,imgOut],2,1):</b> Kameradan alınan orijinal kareyi ve arka planı çıkarılmış kareyi yatay olarak üst üste ekler.
