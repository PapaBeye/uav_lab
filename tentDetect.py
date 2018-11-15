import cv2
import numpy as np
import imutils

def getsquare(image):
    #f = open("demofile.txt", "w") 
    #i = 1
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 230, 255, cv2.THRESH_BINARY)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    for c in cnts:
        
        M = cv2.moments(c)
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        area = cv2.contourArea(c)

        if len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
           
            ar = w / float(h)
            if area > 2000 and ar >= 0.60 and ar <= 1.30:  # 7000 is arbitrary for this purpose its the area of the larget object on test image / 2
                cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
                #f.write(str(area)+"     ,"+str(i)+"  END\n\n\n\n")
                #i += 1

        else:
            pass
        
    rrs = cv2.resize(img, (1280,720))
    cv2.imshow("final", rrs)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        
            
        
        
        
        
    #f.close()
    #rrs = cv2.resize(img, (1280,720))
    #rgray = cv2.resize(gray, (1280,720))
    #rt = cv2.resize(thresh, (1280,720))
    #rb = cv2.resize(blurred, (1280,720))
    #cv2.imshow("final", rrs) # for viewing purposes
    #cv2.imshow("Blurred", rb)
    # #cv2.imshow("Gray", rgray)
    # #cv2.imshow("Thresh", rt)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

# test function
img = 'img1538674924526.jpg'
getsquare(img)

