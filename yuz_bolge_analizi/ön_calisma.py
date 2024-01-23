"""
import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection.FaceDetection( min_detection_confidence=0.1)
mp_drawing = mp.solutions.drawing_utils

webCam= cv2.VideoCapture(0)

while webCam.isOpened():
    succes, frame =webCam.read()

    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = mp_face_detection.process(frame)


    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(frame, detection)


    cv2.imshow("Bolgesel Analiz", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

webCam.release()
cv2.destroyAllWindows()
"""

import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.1)
mp_face_mesh = mp.solutions.face_mesh.FaceMesh(min_detection_confidence=0.1)

mp_drawing = mp.solutions.drawing_utils

webCam = cv2.VideoCapture(0)

while webCam.isOpened():
    success, frame = webCam.read()

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Yüz tespiti
    results_detection = mp_face_detection.process(frame_rgb)
    if results_detection.detections:
        for detection in results_detection.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)

            #mp_drawing.draw_detection(frame, detection)
            cv2.rectangle(frame, bbox, (255, 0, 255), 1)

            # Burun, kulak ve ağız bölgelerini işaretlemek için yüzün landmark'larını al
            results_mesh = mp_face_mesh.process(frame_rgb)
            if results_mesh.multi_face_landmarks:
                for landmarks in results_mesh.multi_face_landmarks:
                    for i, lm in enumerate(landmarks.landmark):
                       
                        x, y = int(lm.x * iw), int(lm.y * ih)

                        # Burun
                        if i == 5:
                            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
                            cv2.putText(frame, "Noise", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1,cv2.LINE_AA)
                        # Sol kulak
                        elif i == 454:
                            cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
                            cv2.putText(frame, "Left Ear", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1,cv2.LINE_AA)
                        # Sağ kulak
                        elif i == 234:
                            cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
                            cv2.putText(frame, "Right Ear", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1,cv2.LINE_AA)
                        # Sol göz
                        elif i == 386:  # Sol göz landmark'ı
                            cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
                            cv2.putText(frame, "Left Eye", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1,cv2.LINE_AA)
                        # Sağ göz
                        elif i == 159:  # Sağ göz landmark'ı
                            cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
                            cv2.putText(frame, "Right Eye", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1,cv2.LINE_AA)
                        # Ağız
                        elif i==13:
                            
                                cv2.circle(frame, (x,y),5, (255, 0, 0), -1)
                                cv2.putText(frame, "Mouth", (x,y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 355, 255), 1, cv2.LINE_AA)


    cv2.imshow("Facial Analysis", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

webCam.release()
cv2.destroyAllWindows()
