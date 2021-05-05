import cv2
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
while True:
    ret, frame = cam.read()
    frame=cv2.rectangle(frame,(140,100),(540,400),(0,255,0),7)
    frame=cv2.circle(frame,(320,240),50,(0,0,0),-1)
    frame=cv2.line(frame, (10,10),(630,470),(0,255,0),4)
    fnt=cv2.FONT_HERSHEY_DUPLEX
    frame=cv2.putText(frame, 'Acid Pandey',(300,300),fnt,1,(255,140,25),2)
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',700,0)

    
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()