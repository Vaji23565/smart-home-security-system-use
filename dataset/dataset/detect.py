import cv2
import numpy as np
import os
import sqlite3
import time
from sms import email_alert

def getprofile(id):
    
    conn=sqlite3.connect("sqlite.db")
    cursor=conn.execute("SELECT * FROM STUDENTS WHERE id =?",(id,))
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile


def detectcam():
    facedetect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    cam=cv2.VideoCapture(0)
    recognizer=cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("recognizer/trainingdata.yml")
    while(True):
        ret,img=cam.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=facedetect.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            id,conf=recognizer.predict(gray[y:y+h,x:x+w])
            profile=getprofile(id)
            #print(profile,conf)
            if(profile!=None):
                if(conf >=50):
                    print("stranger")
                    email_alert("Alert","Some stranger has arrived","ramyaravi654@gmail.com")
                    time.sleep(10)
                else:
                    print(profile[1])
                #cv2.putText(img,"Name:"+str(profile[1]),(x,y+h+20),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,127),2)
                #cv2.putText(img,"Age:"+str(profile[2]),(x,y+h+45),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,127),2)
                
        cv2.imshow("FACE",img);
        if(cv2.waitKey(10)==ord('q')):
            break;
        
    cam.release()
    cv2.destroyAllWindows()
