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

cvLogo=cv2.imread('modi.jpg')
cvLogo=cv2.resize(cvLogo,(160,120))
cv2.imshow('cvLogo',cvLogo)
cv2.moveWindow('cvLogo',700,0)

cvLogoGray=cv2.cvtColor(cvLogo,cv2.COLOR_BGR2GRAY)
cv2.imshow('cv Logo Gray',cvLogoGray)
cv2.moveWindow('cv Logo Gray',700,170)

_,BGMask=cv2.threshold(cvLogoGray,253,255,cv2.THRESH_BINARY)
cv2.imshow('BGMask',BGMask)
cv2.moveWindow('BGMask',700,340)

FGMask=cv2.bitwise_not(BGMask)
cv2.imshow('FGMask',FGMask)
cv2.moveWindow('FGMask',700,510)

FG=cv2.bitwise_and(cvLogo,cvLogo,mask=FGMask)
cv2.imshow('FG',FG)
cv2.moveWindow('FG',700,680)

BW=160
BH=120
Xpos=10
Ypos=10
dy=2
dx=2


while True:
    ret, frame = cam.read()

    ROI=frame[Ypos:Ypos+BH,Xpos:Xpos+BW]
    ROIBG=cv2.bitwise_and(ROI,ROI,mask=BGMask)
    cv2.imshow('ROIBG',ROIBG)
    cv2.moveWindow('ROIBG',900,0)

    ROInew=cv2.add(FG,ROIBG)
    cv2.imshow('ROInew',ROInew)
    cv2.moveWindow('ROInew',900,170)

    frame[Ypos:Ypos+BH,Xpos:Xpos+BW]=ROInew

    Xpos=Xpos+dx
    Ypos=Ypos+dy
    if Xpos+BW >= dispW or Xpos <= 0:
        dx=dx*(-1)
    if Ypos+BH >= dispH or Ypos <= 0:
        dy=dy*(-1)

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()