import cv2
import numpy as np
import sqlite3
faceDetect=cv2.CascadeClassifier('C:\\Users\hp\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read("F:\\Face\\detectionsqllite\\recognizer\\trainingData.yml")

def getProfile(id):
    con=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(id)
    cursor=con.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    con.close()
    return profile

id=0
#font = cv2.cv2.InitFont(cv2.cv2.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontcolor = (0, 255, 0)
while(True):
    ret, img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray, 1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        id, conf=rec.predict(gray[y:y+h, x:x+w])
        profile=getProfile(id)
        if (profile!=None):
            #cv2.cv.putText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255)
            cv2.putText(img, "Name:"+str(profile[1]), (x,y+h+30), fontface, 0.6, fontcolor, 2)
            cv2.putText(img, "Age:"+str(profile[4]), (x,y+h+60), fontface, 0.6, fontcolor, 2)
            cv2.putText(img, "Gender:"+str(profile[2]), (x,y+h+90), fontface, 0.6, fontcolor, 2)
            cv2.putText(img, "Occupation:"+str(profile[3]), (x,y+h+120), fontface, 0.6, fontcolor, 2)

    cv2.imshow("Frame", img)
    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()


