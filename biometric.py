import face_recognition as fr
import cv2
import pandas as pd
import csv
import smtplib as s
from datetime import date
##Self created
import studentdb
import attendanceandmail as atandm


    
v=cv2.VideoCapture(0)
##reading student database
newname=studentdb.read_student_db()[0]
newke=studentdb.read_student_db()[1]
##today's date
d=str(date.today()).split('-')
month=int(d[1])
date=int(d[2])
datetoday=str(date)+'/'+str(month)

##save column of today's date
attendancerecord=pd.read_csv('attendancerecord.csv')
days=list(attendancerecord.columns)
todaysdatecolumnindex=days.index(datetoday)

print( 'Welcome to face biometric attendnce system')
print('Kindly face towards the camera and press "C" to capture your image')
print('Press "y" to exit the camera')
while (1):
    
    returntype,im=v.read()
    
    cv2.imshow('image',im)
    k=cv2.waitKey(5)
    
    if(k==ord('c')):
        
        img=im.copy()
        img=cv2.resize(img,(0,0),fx=0.25,fy=0.25)
        fl=fr.face_locations(img)
        
        if(len(fl)>0):
            e=fr.face_encodings(img,fl)[0]
            face=fr.compare_faces(newke,e)## compare face encodings
            print(face)
            count=0
            for i in range(0,len(face)):
                if face[i]==True:
                    count=count+1
                    print(newname[i])
                    hj=pd.read_csv('attendancerecord.csv')
                    
                    print(datetoday)
                    for f in range (0,hj.shape[0]):
                        if(hj['Name'][f]==newname[i]):
                            print('Present marked')
                            hj[datetoday][f]='p'
                        else:
                            
                            if(hj[datetoday][f]=='p'):
                                print(hj[datetoday][f])
                                hj[datetoday][f]='p'
                            else:
                                
                                hj[datetoday][f]='a'
                            
                            
                    hj.to_csv('attendancerecord.csv', index=None)
             
          
            if (count==0):##if user not found
                with open('faceencode123.csv','a') as newfile:
                    newfilewriter=csv.writer(newfile)
                    newuser=input('Sorry your database not found. Please enter your name')
                    encoding=list(e)
                    newfilewriter.writerow([e,newuser])
                    print('user entered')
                with open('faceencode123emailid.csv','a') as newfile:
                    newfilewriter=csv.writer(newfile)
                    newuseremail=input('Enter your email id')
                    newfilewriter.writerow([newuser,newuseremail])
                    print('email entered')
                with open('attendancerecord.csv','a') as newfile:
                    newfilewriter=csv.writer(newfile)
                    
                    newfilewriter.writerow([newuser])
                    
                    break
                
    
    if(k==ord('y')):
        cv2.destroyAllWindows()
        v.release()
        break
##hj=pd.read_csv(r'C:\Users\hp\Desktop\techieest\attendancerecord.csv')
try:
    hj.to_csv('attendancerecord.csv', index=None)
except:
    pass

gf=pd.read_csv('faceencode123.csv')
emailcsv=pd.read_csv('faceencode123emailid.csv')

##prompt if you want to know the attendance till now date


while(1):
    attendancechoice=input('Enter choice: \n 1.Press t for calculating total attendance and sending a mail \n 2.Press y to quit')
    if(attendancechoice=='t'):
        atandm.attendance(datetoday,todaysdatecolumnindex,days)
    elif(attendancechoice=='y'):
        break
    else:
        print('Enter correct choice')
