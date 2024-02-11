# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:30:45 2023

@author: babak.i
"""

#==========================================================================
#
#   This function is track post request to CRA API
#
#=========================================================================
import requests
import urllib3
import ini
import json
import enc
with open('./molo/molo.pnvt', 'rb') as filekey:
	key = filekey.read()
 
filename='Configuration.ini'

enc.decrypt_fernet(key,filename)
config = ini.parse(open(filename).read())
enc.encrypt_fernet(key,filename)


def create(data):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    headers = {
        "accept": "text/plain",
        "content-Type": "application/json;charset=utf-8"

    }

   


    response=requests.post(config['source']['launch']['restaddsave'], headers=headers, data=json.dumps(data),verify=False)
    return(response.text)
