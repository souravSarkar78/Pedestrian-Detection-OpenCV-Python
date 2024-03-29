import cv2
import numpy as np
import imutils
from imutils.object_detection import non_max_suppression


## Histogram of Oriented Gradients Detector
HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture(0)

def Detector(frame):
    frame = imutils.resize(frame, width=700)
    ## USing Sliding window concept
    rects, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.03)
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.5)
    c = 1

    for x, y, w, h in pick:
        cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 2)
        cv2.rectangle(frame, (x, y - 20), (w,y), (0, 0, 255), -1)
        cv2.putText(frame, f'P{c}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        c += 1

    cv2.putText(frame, f'Total Persons : {c - 1}', (10, 20), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255,255), 2)

    return frame

while True:
    _, frame = cap.read()

    output = Detector(frame)

    cv2.imshow('output', output)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
