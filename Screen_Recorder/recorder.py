import pyautogui
import cv2
import numpy as np

screen_size = (1920, 1080)  # Change this to match your screen resolution
fps = 30
output_filename = "screen_record.avi"

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(output_filename, fourcc, fps, screen_size)

while True:
    # Capture screen content
    frame = pyautogui.screenshot()
    frame = np.array(frame)

    # Convert BGR format (used by OpenCV) to RGB format
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the video file
    out.write(frame)

    # Stop recording when the user presses the 'q' key
    if cv2.waitKey(1) == ord("q"):
        break

out.release()
cv2.destroyAllWindows()