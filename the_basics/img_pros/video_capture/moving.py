import cv2.cv2 as cv2
import time
from datetime import datetime
import pandas

# 0 or 1 or 2 or ..... dependes on how many cameras you have 
# here we only have the internal web cam so it's index is Zero (0)
video = cv2.VideoCapture(0,cv2.CAP_DSHOW)

first_frame = None
start_time = []
end_time = []
status_list = [None,None]
times = []
df = pandas.DataFrame(columns= ["Start","End"])

# Continue means continue from the beingging (not to complete the rest of code)
while(True):
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21,),0)
    if first_frame is None:
        first_frame = gray 
        continue

    
    delta_frame = cv2.absdiff(first_frame , gray)
    
    thresh_frame = cv2.threshold(delta_frame, 30 , 255, cv2.THRESH_BINARY)[1]
    
    thresh_frame = cv2.dilate(thresh_frame,None, iterations=2)
        
    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

   
    for countour in  cnts:
        if cv2.contourArea(countour) < 10000:
            continue
        else:
            status = 1
            if start_time == []:
                 now = datetime.now()
                 start_time.append(now.strftime("%H:%M:%S"))
            now = datetime.now()
            end_time.append(now.strftime("%H:%M:%S"))
        
        (x , y, w, h) = cv2.boundingRect(countour)
        cv2.rectangle(frame,(x,y), (x+w,y+h), (0,255,0),3)
        
    

    status_list.append(status)
    
    if status_list[-1] == 1 and status_list[-2] == 0:
        now = datetime.now()
        times.append(now.strftime("%D %H:%M:%S"))
        
    if status_list[-1] == 0 and status_list[-2] == 1:
        now = datetime.now()
        times.append(now.strftime("%D %H:%M:%S"))
        
    
    cv2.imshow("Gray_Frame",gray)
    cv2.imshow("Delta_frame",delta_frame)
    cv2.imshow("Threshold_frame",thresh_frame)    
    cv2.imshow("Color_Frame",frame)    
  
  
    
    # Close the windows when q pressed
    key = cv2.waitKey(1)
    if key == ord('q'):
        # Here add the last time before close the windows 
        # if the object still moving 
        if status == 1: 
            now = datetime.now()
            times.append(now.strftime("%D %H:%M:%S")) 
        break

video.release()

#print("StartTime",start_time)
#print("EndTime",end_time)
print("times",times)
for i in range(0,len(times),2):
    df = df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

df.to_csv("Times.csv")
cv2.destroyAllWindows()
