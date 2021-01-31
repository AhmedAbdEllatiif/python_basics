import cv2.cv2 as cv2
import time

# 0 or 1 or 2 or ..... dependes on how many cameras you have 
# here we only have the internal web cam so it's index is Zero (0)
video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


a = 0
while(True):
    a = a + 1
    check, frame = video.read()
    #print(frame)

    #time.sleep(1)
   

    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Capturing",gray)
    faces = face_cascade.detectMultiScale(frame,
                                      scaleFactor = 1.05,
                                      minNeighbors = 5)


    for x,y,w,h in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
    
    
    cv2.imshow("Capturing",frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    
    

print(a)
video.release()
cv2.destroyAllWindows()