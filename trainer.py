import os
import cv2
import numpy as np
from PIL import Image

recognizer=cv2.face.LBPHFaceRecognizer_create()
path='F:\\Face\\detectionsqllite\\dataSet'

def getImagesWithID(path):
    imgPaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    Ids=[]
    for imgPath in imgPaths:
        faceImg=Image.open(imgPath).convert("L")
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imgPath)[-1].split('.')[1])
        faces.append(faceNp)
        Ids.append(ID)
        cv2.imshow("traning", faceNp)
        cv2.waitKey(10)
    return np.array(Ids), faces

Ids, faces=getImagesWithID(path)
recognizer.train(faces,Ids)
recognizer.save("recognizer/trainingData.yml")
cv2.destroyAllWindows()
