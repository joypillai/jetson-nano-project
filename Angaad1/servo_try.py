from adafruit_servokit import ServoKit
import cv2
import jetson.inference
import jetson.utils
import time
import numpy as np
import threading

item = ""
top = 0
bottom = 0
left = 0
right = 0



def servo_run():
    myKit=ServoKit(channels=16)

    myKit.servo[0].angle=0
    #time.sleep(3)
    myKit.servo[1].angle=0
    myKit.servo[3].angle=0
    myKit.servo[2].angle=0
    print("Done")
    time.sleep(10)
    print("Done")
    myKit.servo[2].angle=0
    time.sleep(8)
    
    while True:
         
        for i in range(0,180,2):
            myKit.servo[3].angle=i
            print("clockwise 1")
            #print(i)
            time.sleep(0.05)
        time.sleep(1)
        for i in range(180,0,-2):
            myKit.servo[3].angle=i
            print("clockwise 1")
            #print(i)
            time.sleep(0.05)
        time.sleep(1)
    # for i in range(90,70,-1):
    #     myKit.servo[2].angle=i
    #     print("clockwise 2")
    #     print(i)
    #     time.sleep(0.05)

def servo_pick():
    myKit=ServoKit(channels=16)

    for i in range(0,30,1):
        myKit.servo[0].angle=i
        print("clockwise 0")
        print(i)
        time.sleep(0.05)

    for i in range(50,70,1):
        myKit.servo[1].angle=i
        print("clockwise 1")
        print(i)
        time.sleep(0.05)

    for i in range(70,30,-1):   
        myKit.servo[2].angle=i
        print("clockwise 2")
        print(i)
        time.sleep(0.05)


    for i in range(30,0,-1):
        myKit.servo[0].angle=i
        print("anticlockwise 0")
        print(i)
        time.sleep(0.05)

    for i in range(30,70,1):  
        myKit.servo[2].angle=i
        print("clockwise 2")
        print(i)
        time.sleep(0.05)

    for i in range(70,50,-1):
        myKit.servo[1].angle=i
        print("clockwise 1")
        print(i)
        time.sleep(0.05)

def servo_place():
    myKit=ServoKit(channels=16)

    for i in range(50,70,1):
        myKit.servo[1].angle=i
        print("clockwise 1")
        print(i)
        time.sleep(0.05)

    for i in range(70,68,-1):   
        myKit.servo[2].angle=i
        print("clockwise 2")
        print(i)
        time.sleep(0.05)

    for i in range(0,30,1):
        myKit.servo[0].angle=i
        print("clockwise 0")
        print(i)
        time.sleep(0.05)


    for i in range(30,0,-1):
        myKit.servo[0].angle=i
        print("anticlockwise 0")
        print(i)
        time.sleep(0.05)

    for i in range(68,70,1):  
        myKit.servo[2].angle=i
        print("clockwise 2")
        print(i)
        time.sleep(0.05)

    for i in range(70,50,-1):
        myKit.servo[1].angle=i
        print("clockwise 1")
        print(i)
        time.sleep(0.05)
     


if __name__=="__main__":
    servo_run()
