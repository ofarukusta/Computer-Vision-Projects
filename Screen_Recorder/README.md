<div align= "center">
<h1>EKRAN VİDEOSU ALMA UYGULAMASI</h1>
</div>
Proje bünyesinde, ekstra bir uygulama indirmeden bilgisayarda yapılan tüm işlerin ekran videosunun alınması amaçlanmıştır. Kod çalıştırdığı an ekran videosu almaya başlar ve durdurulana kadar almaya devam eder. Daha sonra elde edilen video kodda belirlenen yere kaydedilir.

- <b>pyautogui:</b> Bu kütüphane, ekran görüntülerini yakalamak için kullanılır. pyautogui.screenshot() fonksiyonu ile ekran görüntüsü alınır.

- <b>cv2 (OpenCV):</b> Bu kütüphane, görüntü işleme ve video işleme için kullanılır. Burada, ekran görüntülerini video dosyasına yazmak için kullanılır.

- <b>screen_size:</b> Ekran çözünürlüğünü belirtir.

- <b>fps (frame per second):</b> Saniyedeki kare sayısını belirtir.

- <b>output_filename:</b> Kaydedilecek video dosyasının adını belirtir.

- <b>VideoWriter:</b> OpenCV tarafından sağlanan bu sınıf, video dosyasını oluşturmak ve yazmak için kullanılır.

- <b>cv2.waitKey(1) == ord("q")::</b> Klavyeden "q" tuşuna basıldığında kaydı durdurur.

- <b>out.release():</b> Video dosyasını kapatır.

- <b>cv2.destroyAllWindows():</b> Açık olan tüm OpenCV pencerelerini kapatır.
