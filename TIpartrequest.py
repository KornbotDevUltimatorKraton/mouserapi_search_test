from email import header
import json
from os import access
import re 
from urllib import request

import requests
from requests.structures import CaseInsensitiveDict
import subprocess
from bs4 import BeautifulSoup

tokendata = [] 
headers = CaseInsensitiveDict()
headers1 = CaseInsensitiveDict()
#headers["Content-Type"] = "application/json"

headers["Content-Type"] = "application/x-www-form-urlencoded"
headers1['Content-Type'] = "application/json"
headers1['Authorization'] = "Beaer 44KcYVtW2TLQCwDH2HoXXqIjGLbY"
data = {
       'grant_type':'client_credentials', 
       'client_id':'GuvvS9szjcfibfwVJ98OgSrmu2D8RU91',
       'client_secret':'uXYtG4qXYLNmdwVA',
       
}

print(headers)   
r = requests.post('https://transact.ti.com/v1/oauth/',headers=headers,data=data)
print(r.status_code)
dataout = r.json()
print(dataout)
access_token = list(dataout)
appname = dataout.get(access_token[4])
Token = dataout.get(access_token[0])
developer_email = dataout.get(access_token[5]) #Getting the developer email 
issued_at = dataout.get(access_token[6]) #Getting the access token 
client_id = dataout.get(access_token[7]) #Getting the client id for access token 
print("Appname: ",appname)
print("Token: ",Token)
print("Issued_at: ",issued_at)


data1 = {
    'access_token': '44KcYVtW2TLQCwDH2HoXXqIjGLbY', 
    'token_type': 'bearer', 
    'expires_in': 3599, 
    'scope': '', 
    'application_name': appname, 
    'developer.email': developer_email,  
    'issued_at': '1644903716350', 
    'client_id': client_id, 
}
'''
r1 = requests.get('https://transact.ti.com/v1/products',headers=headers1)
print(r1.status_code)
dataout1 = r1.json() 
print(dataout1)
'''