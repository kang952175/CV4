import cv2
import os


capture = cv2.VideoCapture("./vid/night_sky.mp4")

while True:
    ret, frame = capture.read()

    if (capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("./vid/night_sky.mp4")

    cv2.imshow("VideoFrame", frame)
    if cv2.waitKey(33) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
