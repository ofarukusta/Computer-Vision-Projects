import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.5)
mp_face_mesh = mp.solutions.face_mesh.FaceMesh(min_detection_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils

webcam = cv2.VideoCapture(0)

while webcam.isOpened():
    success, frame = webcam.read()

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results_detection = mp_face_detection.process(frame_rgb)
    if results_detection.detections:
        for detection in results_detection.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)

            cv2.rectangle(frame, bbox, (0, 0, 0), 1)

            results_mesh = mp_face_mesh.process(frame_rgb)
            if results_mesh.multi_face_landmarks:
                for face_landmarks in results_mesh.multi_face_landmarks:
                    # Etiketlenmesi istenilen bölgelerin LandMarklarının girilmesi
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
                            cv2.circle(frame, (x, y), 5, (0, 0, 0), -1)
                            cv2.putText(frame, landmark_points[id], (x, y),
                                        cv2.FONT_HERSHEY_TRIPLEX, 0.3, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow("Facial Analysis", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()
