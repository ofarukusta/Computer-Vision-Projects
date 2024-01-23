import cv2
import mediapipe as mp

# MediaPipe yüz algılayıcısını başlat
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Video akışını başlat
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    # Çerçevedeki yüzleri algıla
    results = face_mesh.process(frame)

    # Sonuçları işleyerek ekrana çizim yapın
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            for i, landmark in enumerate(face_landmarks.landmark):
                ih, iw, _ = frame.shape
                x, y = int(landmark.x * iw), int(landmark.y * ih)
                cv2.circle(frame, (x, y), 1, (0, 255, 0), 1)

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
