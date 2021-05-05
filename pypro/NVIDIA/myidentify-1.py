import jetson.inference 
import jetson.utils

net=jetson.inference.imageNet('googlenet')
cam=jetson.utils.gstCamera(640,480,'/dev/video0')
disp=jetson.utils.glDisplay()
font=jetson.utils.cudaFont()

while disp.IsOpen():
    frame,width,height=cam.CaptureRGBA()
    classID, confident=net.Classify(frame, width, height)
    item=net.GetClassDesc(classID)
    font.OverlayText(frame, width, height, item, 5,5, font.Magenta, font.Blue)
    disp.RenderOnce(frame, width, height)