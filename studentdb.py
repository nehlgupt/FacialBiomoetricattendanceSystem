def read_student_db():
    import pandas as pd
    newke=[]
    gf=pd.read_csv('faceencode123.csv')
    for j in range(0,len(gf['Encoding'])):
        
        
        gfnew=gf['Encoding'][j].replace('\n',',')
        gfnewnew=gfnew.replace(' ',',')
        gfnewnewnew=gfnewnew.replace(',,',',')
        gfnew=gfnewnewnew.replace(',,',',')
        gfnew=gfnew.replace('[','')
        gfnew=gfnew.replace(']','')
        gfnew=gfnew.split(',')
        for i in range(0,len(gfnew)):
              gfnew[i]=float(gfnew[i])
        newke.append(gfnew)


    newname=list(gf['name'])
    return newname,newke
