from adafruit_servokit import ServoKit
import cv2
import jetson.inference
import jetson.utils
import time
import numpy as np
import threading
import RPi.GPIO as GPIO
import _thread
import serial 
import os

item = ""
top = 0
bottom = 0
left = 0
right = 0
pos_servo0=0
pos_servo1=0
pos_servo2=0
pos_servo3=0


def servo_run():
    global pos_servo0
    global pos_servo1
    global pos_servo2
    global pos_servo3
    
    myKit=ServoKit(channels=16)

    myKit.servo[0].angle=0
    #time.sleep(3)
    # myKit.servo[1].angle=0
    # time.sleep(3)
    # myKit.servo[2].angle=30
    # time.sleep(8)
    myKit.servo[3].angle=0
   
    for i in range(0,20,2):
        myKit.servo[2].angle=i
        print("clockwise 1")
        #print(i)
        time.sleep(0.05)
        pos_servo2=i
    time.sleep(1)
         
    for i in range(20,30,2):
        myKit.servo[1].angle=i
        #print("clockwise 1")
        #print(i)
        time.sleep(0.05)
        pos_servo1=i
    time.sleep(1)
   
    # for i in range(90,70,-1):
    #     myKit.servo[2].angle=i
    #     print("clockwise 2")
    #     print(i)
    #     time.sleep(0.05)

def lock_on():
    global item
    global top
    global bottom
    global left
    global right
    global pos_servo0
    global pos_servo1
    global pos_servo2
    global pos_servo3
    toplock = 0
    bottomlock = 0
    rightlock = 0
    leftlock = 0
    stop_arm = 0
    count = 0
    myKit=ServoKit(channels=16)
    while (stop_arm == 0):
        
        
        print("thread 2 running")
        print(item,top,left,bottom,right)

        cx=0
        cy=0
        w=0
        h=0
        area=0

        w=right-left
        h=bottom-top

        cx=left+w/2
        cy=top+h/2

        print(cx,cy)
        if(toplock!=top or bottomlock!=bottom or rightlock!=right or leftlock!=left):
            if(cx>645):
                if(pos_servo3>0):
                    pos_servo3=pos_servo3-1
                    myKit.servo[3].angle=pos_servo3

            elif(cx<635):
                if(pos_servo3<180):
                    pos_servo3=pos_servo3+1
                    myKit.servo[3].angle=pos_servo3

            if(cy>365):
                if(pos_servo1>0):
                    pos_servo1=pos_servo1-1
                    myKit.servo[1].angle=pos_servo1

            elif(cy<355):
                if(pos_servo1<90):
                    pos_servo1=pos_servo1+1
                    myKit.servo[1].angle=pos_servo1
            area=w*h
            if(area<340000):
                pos_servo1=pos_servo1+1
                myKit.servo[1].angle=pos_servo1
                pos_servo2=pos_servo2+1
                myKit.servo[2].angle=pos_servo2
            elif(item=="Redbox" and area>=340000):
                    stop_arm=1
               
                
        leftlock=left
        rightlock=right
        toplock=top
        bottomlock=bottom
        time.sleep(0.05)


def pick_up():
    global pos_servo0
    global pos_servo1
    global pos_servo2
    global pos_servo3
    myKit=ServoKit(channels=16)

    for i in range(0,90,2):
        myKit.servo[0].angle=i
        #print("clockwise 1")
        #print(i)
        time.sleep(0.05)
        pos_servo0=i
         
    for i in range(0,7,1):
        myKit.servo[1].angle=i+pos_servo1
        #print("clockwise 1")
        #print(i)
        time.sleep(0.05)
        pos_servo1=i+pos_servo1

    time.sleep(0.5)

    for i in range(0,6,1):
        myKit.servo[2].angle=i+pos_servo2
        #print("clockwise 1")
        #print(i)
        time.sleep(0.05)
        pos_servo2=i+pos_servo2
    time.sleep(0.5)
    
    for i in range(90,20,-2):
        myKit.servo[0].angle=i
        #print("clockwise 1")
        #print(i)
        time.sleep(0.05)
        pos_servo0=i

    for pos_servo2 in range(pos_servo2,20,-2):
        myKit.servo[2].angle=pos_servo2
        #print("clockwise 1")
        #print(i)
        time.sleep(0.05)
        

def object_detection():

    global item
    global top
    global bottom
    global left
    global right
    timeStamp=time.time()
    fpsFiltered=0

    net=jetson.inference.detectNet(argv=["--model=/home/jetbot/Downloads/jetson-inference/python/training/detection/ssd/models/myModel/ssd-mobilenet.onnx", "--labels=/home/jetbot/Downloads/jetson-inference/python/training/detection/ssd/models/myModel/labels.txt", "--input-blob=input_0", "--output-cvg=scores", "--output-bbox=boxes"], threshold=0.5)
    dispW=1280
    dispH=720
    flip=2

    font=cv2.FONT_HERSHEY_SIMPLEX
    #cam=jetson.utils.gstCamera(dispW,dispH,'/dev/video0')
    #display=jetson.utils.glDisplay()

    cam=cv2.VideoCapture('/dev/video0')
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)
    #while display.IsOpen():
        #img,width,height=cam.CaptureRGBA()
    while True:
        _,img = cam.read()
        height=img.shape[0]
        width=img.shape[1]

        frame=cv2.cvtColor(img,cv2.COLOR_BGR2RGBA).astype(np.float32)
        frame=jetson.utils.cudaFromNumpy(frame)

        detections=net.Detect(frame,width,height)
        for detect in detections:
            #print(detect)
            ID=detect.ClassID
            top=int(detect.Top)
            left=int(detect.Left)
            bottom=int(detect.Bottom)
            right=int(detect.Right)
            item=net.GetClassDesc(ID)
            # print(item,top,left,bottom,right)
            #time.sleep(1)
            cv2.rectangle(img,(left,top),(right,bottom),(255,0,0),2)
            cv2.putText(img,item,(left,top+20),font,.75,(0,0,255),2)
        #display.RenderOnce(frame,width,height)
        dt=time.time()-timeStamp
        timeStamp=time.time()
        fps=1/dt
        fpsFiltered=0.9*fpsFiltered+.1*fps
        print(str(round(fps,1))+' fps')

        cv2.putText(img,str(round(fpsFiltered,1))+' fps',(0,30),font,1,(0,0,255),2)
        cv2.imshow('detCam',img)
        cv2.moveWindow('detCam',0,0)
        if cv2.waitKey(1)==ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    thread1 = threading.Thread(target=object_detection)
    thread2 = threading.Thread(target=lock_on)
    servo_run()
    thread1.start()
    # while True:
    #     lock_on_object()
    thread2.start()
    thread2.join()
    pick_up()
    
