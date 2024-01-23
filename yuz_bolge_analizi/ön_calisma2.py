import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.5)
mp_face_mesh = mp.solutions.face_mesh.FaceMesh(min_detection_confidence=0.5)

# Görselin tanımlanıp, RGB hale getirilmesi
image = cv2.imread("salah.jpeg")
image = cv2.flip(image,1)

# Yüz Tespiti
results_detection = mp_face_detection.process(image)
if results_detection.detections:
    for detection in results_detection.detections:
        bboxC = detection.location_data.relative_bounding_box
        ih, iw, _ = image.shape
        
        bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
               int(bboxC.width * iw), int(bboxC.height * ih)
        cv2.rectangle(image, bbox, (0, 0, 0), 1)

        result_mesh = mp_face_mesh.process(image)
        if result_mesh.multi_face_landmarks:
            for face_landmarks in result_mesh.multi_face_landmarks:
                #İstenilen bölgelerin ve landmarklarının listelenmesi
                landmark_points = {
                    5: "Nose",
                    159: "Right Eye",
                    386: "Left Eye",
                    234: "Right Ear",
                    454: "Left Ear",
                    13: "Mouth"
                }

                for id, lm in enumerate(face_landmarks.landmark):
                    if id in landmark_points:
                        x, y = int(lm.x * iw), int(lm.y * ih)
                        cv2.circle(image, (x, y), 5, (0, 0, 0), -1)
                        cv2.putText(image, landmark_points[id], (x, y),
                                    cv2.FONT_HERSHEY_TRIPLEX, 0.3, (255, 255, 255), 1, cv2.LINE_AA)

# Sonuçları göster
cv2.imshow("Facial Analysis", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

output_image_path = "output_image.jpg"
cv2.imwrite(output_image_path, image)
print("İşlenmiş görüntü kaydedildi:", output_image_path)