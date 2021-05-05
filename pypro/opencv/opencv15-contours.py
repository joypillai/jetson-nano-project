import cv2
print(cv2.__version__)
import numpy as np

def nothing(x):
    pass

dispW=640
dispH=480
flip=2

#Uncomment These next Two Line for Pi Camera
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam= cv2.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',1320,0)

cv2.createTrackbar('hueLower','Trackbars',103,179,nothing)
cv2.createTrackbar('hueUpper','Trackbars',127,179,nothing)
cv2.createTrackbar('hueLower2','Trackbars',90,179,nothing)
cv2.createTrackbar('hueUpper2','Trackbars',100,179,nothing)
cv2.createTrackbar('satLow','Trackbars',157,255,nothing)
cv2.createTrackbar('satHigh','Trackbars',255,255,nothing)
cv2.createTrackbar('valLow','Trackbars',120,255,nothing)
cv2.createTrackbar('valHigh','Trackbars',255,255,nothing)




cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
while True:
    ret, frame = cam.read()
    #frame=cv2.imread('smarties.png')
    


    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    Lh=cv2.getTrackbarPos('hueLower','Trackbars')
    Uh=cv2.getTrackbarPos('hueUpper','Trackbars')
    Lh2=cv2.getTrackbarPos('hueLower2','Trackbars')
    Uh2=cv2.getTrackbarPos('hueUpper2','Trackbars')
    Ls=cv2.getTrackbarPos('satLow','Trackbars')
    Us=cv2.getTrackbarPos('satHigh','Trackbars')
    Lv=cv2.getTrackbarPos('valLow','Trackbars')
    Uv=cv2.getTrackbarPos('valHigh','Trackbars')

    l_b=np.array([Lh,Ls,Lv])
    u_b=np.array([Uh,Us,Uv])

    l_b2=np.array([Lh2,Ls,Lv])
    u_b2=np.array([Uh2,Us,Uv])

    FGmask=cv2.inRange(hsv,l_b,u_b)
    FGmask2=cv2.inRange(hsv,l_b2,u_b2)
    FGmaskComp=cv2.add(FGmask,FGmask2)
    cv2.imshow('FGmaskComp',FGmask)
    cv2.moveWindow('FGmaskComp',0,410)

    contours,_=cv2.findContours(FGmaskComp,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    #cv2.drawContours(frame,contours,0,(255,0,0),3)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        (x,y,w,h)=cv2.boundingRect(cnt)
        if area>=500:
            #cv2.drawContours(frame,[cnt],0,(255,0,0),3)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)

    cv2.moveWindow('final',900,0)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()