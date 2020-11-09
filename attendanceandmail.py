
##Code for attendance and mail sending
import pandas as pd
import smtplib as s


def attendance(datetoday,todaysdatecolumnindex,days):
    jk=pd.read_csv('attendancerecord.csv')
    name=input('Enter the name of student')
    
    count=0
    for r in range(0,jk.shape[0]):
        if(jk['Name'][r]==name):
            count=count+1
            presentcount=0
            for m in range(0,(todaysdatecolumnindex+1)):
                
                if(jk[days[m]][r]=='p'):
                    presentcount=presentcount+1
            totalattendance=(presentcount/(todaysdatecolumnindex))*100
            print('Total attendance of '+ name + ' is ' + str(totalattendance))
            mailsending(datetoday,totalattendance,name)
    if(count==0):
        print('Enter name correctly')
def mailsending(datetoday,totalattendance,name):
    mailchoice=input('Do you want to send an email (y/n)?')
    if(mailchoice=='y'):
        g=s.SMTP('smtp.gmail.com',587)
        print('start')
        reciepentname=name
        eml=pd.read_csv('faceencode123emailid.csv')
        
        for r in range(0,eml.shape[0]):
            if(eml['Name'][r]==reciepentname):
                emailid=eml['emailid'][r]
                print('concatenating message')
                message='The attendance of ' + eml['Name'][r] + ' is ' + str(totalattendance) + ' till date ' + datetoday
                print(message)
                g.starttls()
                g.login('nehalg2@gmail.com','567tyu567tyu')
                print('login successfully')
                g.sendmail('nehalg2@gmail.com',emailid,message)
                g.close()
                print('mail sent successfully')
                
        
        
    elif(mailchoice=='n'):
        pass
    else:
        print('Enter correct choice')
    
	
    
