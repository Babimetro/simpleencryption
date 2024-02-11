
import ini
import pymssql
import datetime
import json
import os
import post
import enc
with open('./molo/molo.pnvt', 'rb') as filekey:
	key = filekey.read()
 
filename='Configuration.ini'

enc.decrypt_fernet(key,filename)
config = ini.parse(open(filename).read())
enc.encrypt_fernet(key,filename)

delta=0
tod = datetime.date.today()
today=str( tod-datetime.timedelta(days = delta))
#============================================


print("Initialization Done")  
url='.\\jason\\'
filelist=os.listdir(url)
for jfile in filelist:

    jf = open(url+jfile)
    dataa=json.load(jf)
    jsone=json. loads(post.create(dataa))
    print(jfile,jsone)
    
    success=jsone["success"]
    message=jsone["message"]
    result=jsone["result"]['tracking']
    
    
    print('success=',success)
    print("message=",message)
    print("result=",result)
    
    
    if success==True:
    
        connection= pymssql.connect(server=config['source']['ios']['server'], user=config['source']['ios']['user'], password=config['source']['ios']['password'], database=config['source']['ios']['database'])
    
        cur = connection.cursor()
        update_list_sql="""UPDATE [dbo].[CRA_EI_Tracker]
              SET [CRA_TrackingNo] = %s
                  ,[Raise_Date]=%s
                  ,[Modified_By]='shakila.k@mtnirancell.ir'
              where [MVO_TrackingNo]=%s"""
        f=len(jfile)
        k=f-5
        Mvo_Trackingcode=jfile[0:k]
        cur.execute(update_list_sql,(result,today,Mvo_Trackingcode))
        connection.commit()
    
    
    print(Mvo_Trackingcode,jsone)
    
    print('Terminated becase of above Error')
    

