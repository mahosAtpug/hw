# First we are going to capture the background video frame
# Second we Tell the code to recognize the red color
# We need to generate a mask
# We need to create the final output to create a magical output

import cv2
import numpy as np
import time

video = cv2.VideoCapture(0)
img = cv2.imread("hw.jpg")

while True:
    ret , frame = video.read()
    frame = cv2.resize(frame , (640 , 480))
    img = cv2.resize(img , (640 , 480))

    u_black = np.array([104 , 153 , 70])
    l_black = np.array([30 , 30 , 0])
    mask = cv2.inRange(frame , l_black , u_black)
    res = cv2.bitwise_and(frame , frame , mask = mask)
    f = frame-res
    f = np.where(f == 0 , img , f)
    cv2.imshow("Video" , frame)
    cv2.imshow("Mask" , f)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

video.release()
out.release()
cv2.destroyAllWindows()

