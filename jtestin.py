import numpy as np
import cv2
import imutils
cap = cv2.VideoCapture(0)

while 1:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 240, 255, cv2.THRESH_BINARY)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    for c in cnts:
        M = cv2.moments(c)
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        area = cv2.contourArea(c)
        if len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
                    # 7000 is arbitrary for this purpose its the area of the larget object on test image / 2
            r = w / float(h)
            if area > 150 and r >= 0.60 and r <= 1.30:
                cv2.drawContours(img, [c], -1, (0, 255, 0), 2)

    
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


'''
def grab_cam():
    while(True):
        ret, frame = cap.read()
        if ret:

            return frame


def getsquare(image):
    #f = open("demofile.txt", "w")
    #i = 1
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 230, 255, cv2.THRESH_BINARY)[1]
    cnts = cv2.findContours(
        thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    for c in cnts:

        M = cv2.moments(c)
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        area = cv2.contourArea(c)

        if len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)

            ar = w / float(h)
            # 7000 is arbitrary for this purpose its the area of the larget object on test image / 2
            if area > 2000 and ar >= 0.60 and ar <= 1.30:
                cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
                #f.write(str(area)+"     ,"+str(i)+"  END\n\n\n\n")
                #i += 1

        else:
            pass

    rrs = cv2.resize(img, (1280, 720))
    cv2.imshow("final", rrs)

img = grab_cam()
getsquare(img)

cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()
'''
#grab_frame()
cap.release()
cv2.destroyAllWindows()
