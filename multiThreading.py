import cv2
#import threading
import multiprocessing
from multiprocessing import pool
import os
import numpy as np
import serial
import imutils
import sys
import VACSParser
import time

if len(sys.argv) != 5:
    print("Usage: python multiThreading.py station-ID gsPIport fcPIport message_definition_path")
    sys.exit(1)
else:
    stid = sys.argv[1]
    gscomport = sys.argv[2]
    fccomport = sys.argv[3]
    message_definition_path = sys.argv[4]


q = multiprocessing.Queue()

class mainsys:
    def __init__(self, stid, gscomport, fc, message_definition_path):
        if stid == 'GS':
            self.gscomtopi = serial.Serial(str(gscomport), baudrate=57600, parity=serial.PARITY_NONE, 
                                           stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
        if stid == 'PI':
            self.gscomtopi = serial.Serial(str(gscomport), baudrate=57600, parity=serial.PARITY_NONE,
                                           stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
            self.fccomport = serial.Serial(str(fccomport), baudrate=57600,)
            self.fcbyte = self.fccomport.read(1) #
            self.vcap = cv2.VideoCapture(0)
            self.isimg_frame = self.vcap.read()
            self.message_definition_path = message_definition_path
            self.turncamoff = self.vcap.release()
            self.parser = VACSParser.Parser(self.message_definition_path)
            self.Altitude = 0.00
            self.Latitude = ''
            self.Longitude = ''
            self.objectdist = 0
            self.frun = True
            self.tentWidth = 20


class rpisys(mainsys):

    def dis_to_camera(self, Width, focalLength, perWidth):
        # compute and return the distance from the maker to the camer
        return (Width * focalLength) / perWidth

    def getFCdata(self):
        while 1:
            try:
                byte = self.fcbyte
                if byte:
                    self.parser.parse(byte)
                    newbyte = self.parser.get_packet()
                    if newbyte:
                        for i in newbyte.message:
                            if i == 'position/longitude':
                                self.Longitube = str(newbyte.message[i])
                                #print("Longitube: "+str(newbyte.message[i]))
                            if i == 'position/latitude':
                                self.Latitude = str(newbyte.message[i])
                                #print("Latitude: "+str(newbyte.message[i]))
                            if i == 'position/altitude':
                                self.Altitude = float(newbyte.message[i])
                                #print("Altitude: "+str(newbyte.message[i]))
            except Exception as e:
                print(e)
                self.getFCdata()


    def find_whiterec_fame(self):
        while 1:
            # self.isimg_frame
            print('at leat i ran')
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
                    r = w / float(h) # 2000 is arbitrary for this purpose its the area of the larget object on test image / 2
                    if area > 2000 and r >= 0.70 and r <= 1.30:
                        cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
                        marker = cv2.minAreaRect(c)
                        if self.frun == True:
                            self.focalLength = (marker[1][0] * self.Altitude) / self.tentWidth
                            self.frun = False
                        self.objectdist = self.distance_to_camera(self.tentWidth, self.focalLength, marker[1][0])
                        self.handleimg(img, 1, str(self.Altitude * 1000))
                else:
                    self.handleimg(img, 0, str(time.time()))
            cv2.imshow('img', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    def handleimg(self, image, xint, name):
        if xint == 1:
            if not os.path.exists('positive'):
                os.makedirs('positive')
            cv2.imwrite("positive/img"+name+".jpg", image)
        elif xint == 0:
            if not os.path.exists('negative'):
                os.makedirs('negative')
            name = time.time() * 1000
            cv2.imwrite("negative/img"+str(name)+".jpg", image)
    def comtogs(self, alt, lon, lat):
        while True:
            if self.gscomtopi.inWaitting() > 0:
                pass
            else:
                data = 'Altid'
                self.gscomtopiw
                pass


'''
            cv2.imshow('img', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
'''

class ground(mainsys):
    pass
while 1:
    rpisys(stid,gscomport, fccomport,message_definition_path).find_whiterec_fame()
    print('haha')