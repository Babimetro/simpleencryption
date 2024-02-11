
#============================================================
#libraries
import ini
import enc
import datetime
'''Hesam jan I stored key in ./molo/molo.pnvt file , 
you can put anything, every where you want
you can also ask user to enter any time'''

with open('./molo/molo.pnvt', 'rb') as filekey:
	key = filekey.read()
#=========================================================    

'''Now you have your config file'''
filename='Configuration.ini'
#============================================
'''
you encypt it for first initiation time.
next time you runn the program you make as commment this part,
only for first time or config change you run it.'''
enc.encrypt_fernet(key,filename)
#========================================
'''This is for '''

enc.decrypt_fernet(key,filename)
config = ini.parse(open(filename).read())
enc.encrypt_fernet(key,filename)

delta=0
tod = datetime.date.today()
today=str( tod-datetime.timedelta(days = delta))
#============================================


print("Initialization Done")  
print(today)
server=config['source']['ios']['server']
user=config['source']['ios']['user']
password=config['source']['ios']['password']
database=config['source']['ios']['database']
print(server,user,password,database)
    

