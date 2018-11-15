import cv2
import numpy as np

#cap = cv2.VideoCapture(0)

#while(1):
frame = cv2.imread('pics/img1538674924526.jpg')
ret, tr = cv2.threshold(frame, 250, 255, cv2.THRESH_BINARY)
hsv = cv2.cvtColor(tr, cv2.COLOR_BGR2HSV)
    
lower_white = np.array([0,0,0], dtype=np.uint8)
upper_white = np.array([0,0,255], dtype=np.uint8)
    
mask = cv2.inRange(hsv, lower_white, upper_white)
res = cv2.bitwise_and(frame,frame, mask= mask)

edges = cv2.Canny(mask,25,25)

rtr = cv2.resize(edges, (1280,720))
rframe = cv2.resize(frame, (1280,720))
rmask = cv2.resize(mask, (1280,720))
rrs = cv2.resize(res, (1280,720))

cv2.imshow('frame',rframe)
#cv2.imshow('mask',rmask)
#cv2.imshow('cl',rrs)
cv2.imshow('edges',rtr)
    
cv2.waitKey(0)

cv2.destroyAllWindows()
#cap.release()

