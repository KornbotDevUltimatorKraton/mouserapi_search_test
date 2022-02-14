import json 
from urllib import request

import requests
from requests.structures import CaseInsensitiveDict
import subprocess
from bs4 import BeautifulSoup


headers = CaseInsensitiveDict()
#headers["Content-Type"] = "application/json"
headers["Content-Type"] = "application/x-www-form-urlencoded"


data = {
       'grant_type':'client_credentials', 
       'client_id':'GuvvS9szjcfibfwVJ98OgSrmu2D8RU91',
       'client_secret':'uXYtG4qXYLNmdwVA',
       
}


r = requests.post('https://transact-pre.ti.com/v1/oauth/',headers=headers,data=data)
print(r.status_code)
dataout = r.json()
print(dataout)
print(headers)
