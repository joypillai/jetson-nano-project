import jetson.inference
import jetson.utils
import cv2
import numpy as np
import time
width=1280
height=720
flip=2
cam=cv2.VideoCapture('/dev/video0')
#display=jetson.utils.glDisplay()
#font=jetson.utils.cudaFont()
net=jetson.inference.imageNet('alexnet')
font=cv2.FONT_HERSHEY_SIMPLEX

timeMark=time.time()
fpsFilter=0
while True:
    #frame,width,height=cam.CaptureRGBA(zeroCopy=1)
    _,frame=cam.read()
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA).astype(np.float32)
    img=jetson.utils.cudaFromNumpy(img)
    classID,confidence=net.Classify(img,width,height)
    item=net.GetClassDesc(classID)
    dt=time.time()-timeMark
    fps=1/dt
    fpsFilter=.95*fpsFilter+.05*fps
    timeMark=time.time()
    #font.OverlayText(frame,width,height,str(round(fpsFilter,1))+' fps '+item,5,5,font.Magenta,font.Blue)
    #display.RenderOnce(frame,width,height)
    frame=jetson.utils.cudaToNumpy(img,width,height,4)
    frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR).astype(np.uint8)
    cv2.putText(frame,str(round(fpsFilter,1))+' fps '+item,(0,30),font,1,(0,0,255),2)
    cv2.imshow('reCam',frame)
    cv2.moveWindow('reCam',0,0)
    if(cv2.waitKey(1)==ord('q')):
        break
cam.releast()
cam.destroyAllWindows()