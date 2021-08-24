from adafruit_servokit import ServoKit
import cv2
import jetson.inference
import jetson.utils
import time
import numpy as np
import threading

myKit=ServoKit(channels=16)

# myKit.servo[0].angle=0
# #time.sleep(3)
# myKit.servo[1].angle=30
# myKit.servo[3].angle=0
# myKit.servo[2].angle=0
while True:
    for i in range(90,0,-2):   
            myKit.servo[1].angle=i
            # print("clockwise 2")
            # print(pos_servo2)
            time.sleep(0.05)
    for i in range(0,90,2):   
            myKit.servo[1].angle=i
            # print("clockwise 2")
            # print(pos_servo2)
            time.sleep(0.05)