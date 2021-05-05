import cv2
import numpy as np
print(cv2.__version__)
dispW=640
dispH=480
flip=2
#Uncomment These next Two Line for Pi Camera
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam= cv2.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
blank=np.zeros([480,640,1],np.uint8)
while True:
    ret, frame = cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(frame[100,100,0])
    #print(frame.shape)
    #print(frame.size)
    
    #print(gray.shape)
    #print(gray.size)

    b=cv2.split(frame)[0]
    g=cv2.split(frame)[1]
    r=cv2.split(frame)[2]

    blue=cv2.merge((b,blank,blank))
    green=cv2.merge((blank,g,blank))
    red=cv2.merge((blank,blank,r))

    cv2.imshow('blue',blue)
    cv2.moveWindow('blue',700,0)

    cv2.imshow('green',green)
    cv2.moveWindow('green',700,700)

    cv2.imshow('red',red)
    cv2.moveWindow('red',0,700)

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)

    cv2.imshow('blank',blank)
    cv2.moveWindow('blank',1400,0)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()