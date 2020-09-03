import numpy as np
import cv2
from PIL import Image



face_cascade = cv2.CascadeClassifier('cars.xml')

#eye_cascade = cv2.CascadeClassifier('cars.xml')

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
	#imwrite(roi_color)
        #Now we will calculate the distance using the triangular similarity menthod
        width=roi_color.size
        height, width, channels = roi_color.shape
        f=170
        #f=d*p
        p=width
        d1=(31.5*f)/p
        #method ends here
        #displaying the Region of intrest with distane in cm
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,str(d1)+' cm',(x,y), font, 1,(255,130,0),2,cv2.LINE_AA)

        #Displaing warning messages as per the distance
        if d1<50 and d1>30:
            #cv2.putText(img,str(d1)+'cm',(x,y), font, 1,(255,0,0),2,cv2.LINE_AA)
            cv2.putText(img,'Proceed with CAUTION',(x,y+200), font, 1,(0,120,255),2,cv2.LINE_AA)
        elif d1<30:
            #cv2.putText(img,str(d1)+'cm',(x,y), font, 1,(255,0,0),2,cv2.LINE_AA)
            cv2.putText(img,'Danger,STOP',(x,y+200), font, 1,(0,0,255),2,cv2.LINE_AA)
		

		


                
        

    cv2.imshow('Lane assistane using object detection',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
