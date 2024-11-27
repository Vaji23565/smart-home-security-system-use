import cv2
import numpy as np
import sqlite3






def insertorupdate(Id,Name,age):
    conn=sqlite3.connect("sqlite.db")
    cmd="SELECT * FROM STUDENTS WHERE ID="+str(Id);
    cursor=conn.execute(cmd);
    isRecordExist=0;
    for row in cursor:
        isRecordExist=1;
    if(isRecordExist==1):
        conn.execute("UPDATE STUDENTS SET NAME=? WHERE ID=?",(Name,Id,))
        conn.execute("UPDATE STUDENTS SET age=? WHERE ID=?",(age,Id,))
    else:
        conn.execute("INSERT INTO STUDENTS (Id,Name,age) values(?,?,?)",(Id,Name,age))

    conn.commit()
    conn.close()


#inser user defined values into table




#detect face in web camera coding
def captureimage():
    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    cam=cv2.VideoCapture(0);
    Id=input('Enter User Id :')
    Name=input('Enter User Name :')
    age=input('Enter User Age :')
    insertorupdate(Id,Name,age)
    sampleNum=0;                         #assume there is no sample in dataset
    while(True):
        ret,img=cam.read();               #OPEN CAMERA
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)          #IMAGE CONVERT INTO BGRGRAY COLOR
        faces=faceDetect.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            sampleNum=sampleNum+1;         #if face is detected increments
            cv2.imwrite("dataset/user."+str(Id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.waitKey(100)                #delay time
        cv2.imshow("Face",img)
        cv2.waitKey(1);
        if(sampleNum>50):
            break;
    cam.release()
    cv2.destroyAllWindows()             #quit

        
    
    

        
    


 
