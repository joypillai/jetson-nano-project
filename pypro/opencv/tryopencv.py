import cv2
import jetson.utils
import jetson.inference

model = jetson.inference.detectNet()
width = 640
height = 320

cam = cv2.VideoCapture('/dev/video0')
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width )
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height )

# Opening the camera
while cam.isOpened():

    ret, frame = cam.read()
    frame_rgba = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA).astype(np.float32)

    img = jetson.utils.cudaFromNumpy(frame_rgba)

    detections = model.Detect(img, width, height, "box,labels,conf")
    conv1 = jetson.utils.cudaToNumpy(img, width, height, 4)        
    conv2 = cv2.cvtColor(conv1, cv2.COLOR_RGBA2RGB).astype(np.uint8)
    conv3 = cv2.cvtColor(conv2, cv2.COLOR_RGB2BGR)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()