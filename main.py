import cv2
import os
import pandas as pd
from datetime import datetime
import csv

video=cv2.VideoCapture('carvideo.mp4')
# video=cv2.VideoCapture(0,cv2.CAP_DSHOW)

car_cascade=cv2.CascadeClassifier('cars.xml')
a=1
while True:
    a=a+1
    status=0    
    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars=car_cascade.detectMultiScale(gray,1.7,1)
    for (x,y,w,h) in cars:
        plate=frame[y : y + h,x : x + w]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame, 'Car', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        cv2.imshow('Car',plate)
        status=1
    cv2.imshow('Car Dectection',frame)
    par=r'C:\Users\laksh\OneDrive\Desktop\desk\traffic2\Images0'
    for i in range(a+1):
        name="Car"+str(i)+".png"
    if (status==1):
        cv2.imwrite(os.path.join(par,name),plate)
        with open('data_logs.csv','a') as f:
            writer=csv.writer(f)
            writer.writerow([name,str(datetime.now())])
        pass

    if cv2.waitKey(33)==ord('q'):
        break

cv2.destroyAllWindows()