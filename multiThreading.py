import cv2
import threading
import numpy as np
import serial
import imutils
import sys
import VACSParser
import time

if len(sys.argv) != 5:
    print("Usage: python multiThreading.py station-ID gspiport fcport message_definition_path")
    sys.exit(1)
else:
    stid = sys.argv[1]
    gscomport = sys.argv[2]
    fccomport = sys.argv[3]
    message_definition_path = sys.argv[4]




class mainsys:
    def __init__(self, stid, gscomport, fc, message_definition_path):
        if stid == 'GS':
            self.gscomtopi = serial.Serial(str(gscomport), baudrate=57600, parity=serial.PARITY_NONE, 
                                           stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
        if stid == 'PI':
            #self.gscomtopi = serial.Serial(str(gscomport), baudrate=57600, parity=serial.PARITY_NONE,
            #                               stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
            #self.fccomport = serial.Serial(str(fccomport), baudrate=57600,)
            self.vcap = cv2.VideoCapture(0)
            self.isimg_frame = self.vcap.read()
            #self.message_definition_path = message_definition_path
            self.turncamoff = self.vcap.release()


class rpisys(mainsys):

    def find_whiterec_fame(self):
        while 1:
            _, img = self.isimg_frame
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            thresh = cv2.threshold(blurred, 230, 255, cv2.THRESH_BINARY)[1]
            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if imutils.is_cv2() else cnts[1]
            for c in cnts:
                M = cv2.moments(c)
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.04 * peri, True)
                area = cv2.contourArea(c)
                if len(approx) == 4:
                    (x, y, w, h) = cv2.boundingRect(approx)
                    r = w / float(h) # 7000 is arbitrary for this purpose its the area of the larget object on test image / 2
                    if area > 2000 and r >= 0.60 and r <= 1.30:
                        cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
                        if not os.path.exists('positive'):
                            os.makedirs('positive')
                        name = time.time * 1000
                        cv2.imwrite("positive/img"+str(name)+".jpg", img)
'''
            cv2.imshow('img', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
'''

class ground(mainsys):
    pass


while not (cv2.waitKey(1) & 0xFF == ord('q')):
    rpisys(stid,gscomport,fccomport, message_definition_path).find_whiterec_fame()
