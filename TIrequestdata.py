from email import header
import json
import re 
from urllib import request

import requests
from requests.structures import CaseInsensitiveDict
import subprocess
from bs4 import BeautifulSoup


headers = CaseInsensitiveDict()
headers1 = CaseInsensitiveDict()
#headers["Content-Type"] = "application/json"
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers1['Content-Type'] = "application/json"
data = {
       'grant_type':'client_credentials', 
       'client_id':'GuvvS9szjcfibfwVJ98OgSrmu2D8RU91',
       'client_secret':'uXYtG4qXYLNmdwVA',
       
}

print(headers)   
r = requests.post('https://transact-pre.ti.com/v1/oauth/',headers=headers,data=data)
print(r.status_code)
dataout = r.json()
print(dataout)
access_token = list(dataout)
appname = dataout.get(access_token[4])
Token = dataout.get(access_token[0])
print("Appname: ",appname)
print("Token: ",Token)

data1 = {
    'access_token':'Zo0M7ADHhuNSDMrB2WRwdCRXnXMG', 
    'token_type': 'bearer', 
    'expires_in': 3599, 
    'scope': '', 
    'application_name': 'roboreactor', 
    'developer.email': 'kornbot380@hotmail.com', 
    'issued_at': '1644993771581', 
    'client_id': 'GuvvS9szjcfibfwVJ98OgSrmu2D8RU91'
}
requestpart = {
 'Page':0,
 'Size':1,
'ProductFamilyDescription':'RF-samplin transceivers',
'GenericProductIdentifier':'AFE7799',
}
url_parts = '?Page=0&Size=1&ProductFamilyDescription=BLDC%20motor%20driver&GenericProductIdentifier=drv8428e'
headers1['Authorization'] = "Bearer "+Token

r1 = requests.get('https://transact-pre.ti.com/v1/products'+url_parts,headers=headers1) 
print(r1.status_code)
dataout1 = r1.json() 
print(dataout1)

