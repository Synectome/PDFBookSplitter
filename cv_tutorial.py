import cv2
import os
import numpy as np

cap = cv2.VideoCapture(0)
count = 0
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    retval, threshold = cv2.threshold(frame, 12, 255, cv2.THRESH_BINARY)
    count += 1
    cv2.imshow('gray', gray)
    cv2.imshow('threshold', threshold)
    # cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print(count)
    if count == 1:
        break

#cap.release()
#cv2.destroyAllWindows()