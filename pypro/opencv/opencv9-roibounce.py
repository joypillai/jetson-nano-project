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
BW=int(0.69*dispW)
BH=int(0.1*dispH)
posX = 10
posY = 10
dx=2
dy=2

while True:
    ret, frame = cam.read()
    roi=frame[posY:posY+BH,posX:posX+BW].copy()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame=cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    frame[posY:posY+BH,posX:posX+BW]=roi
    cv2.rectangle(frame,(posX,posY),(posX+BW,posY+BH),(255,0,255),7)
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    posX=posX+dx
    posY=posY+dy
    if (posX+BW > dispW):
        dx=dx*(-1)
    elif posY+BH > dispH:
        dy=dy*(-1)
    elif posX < 0:
        dx=dx*(-1)
    elif posY < 0:
        dy=dy*(-1)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()