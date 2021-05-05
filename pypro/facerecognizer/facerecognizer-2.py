import face_recognition
import cv2
print(cv2.__version__)

polFace=face_recognition.load_image_file('/home/jetbot/Desktop/pypro/facerecognizer/demoImages/known/Paul McWhorter.jpg')
polEncode=face_recognition.face_encodings(polFace)[0]

Encodings=[polEncode]
Names=['The Bhuddha']

font=cv2.FONT_HERSHEY_SIMPLEX
test_image=face_recognition.load_image_file('/home/jetbot/Desktop/pypro/facerecognizer/demoImages/unknown/u13.jpg')
facePositions=face_recognition.face_locations(test_image)
allEncodings=face_recognition.face_encodings(test_image,facePositions)

test_image=cv2.cvtColor(test_image,cv2.COLOR_RGB2BGR)

for (top,right,bottom,left), face_encoding in zip(facePositions,allEncodings):
    name='Unknown Person' 
    matches=face_recognition.compare_faces(Encodings,face_encoding)
    if True in matches:
        first_match_index=matches.index(True)
        name=Names[first_match_index]    
    cv2.rectangle(test_image,(left,top),(right,bottom),(0,0,255),4)
    cv2.putText(test_image,name,(left,top-6),font,.75,(255,0,255),1)
cv2.imshow('window',test_image)
cv2.moveWindow('window',0,0)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()