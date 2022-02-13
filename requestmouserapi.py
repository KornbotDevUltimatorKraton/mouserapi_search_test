import json 
from urllib import request

import requests
from requests.structures import CaseInsensitiveDict
import subprocess
curl = 'curl -X POST "https://api.mouser.com/api/v1/search/partnumber?apiKey=cf621336-fea9-4734-81dd-a8442ed3e05c" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"SearchByPartRequest\": { \"mouserPartNumber\": \"LM324\", \"partSearchOptions\": \"1\" }}"'
curl1 = 'curl -X POST "https://api.mouser.com/api/v1/search/keyword?apiKey=cf621336-fea9-4734-81dd-a8442ed3e05c" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"SearchByKeywordRequest\": { \"keyword\": \"DC motor driver IC\", \"records\": 0, \"startingRecord\": 0, \"searchOptions\": \"1\", \"searchWithYourSignUpLanguage\": \"English\" }}"'
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = { 
  'apiKey':'cf621336-fea9-4734-81dd-a8442ed3e05c',
  'SearchByKeywordRequest': {
    'keyword': 'DC motor driver IC',
    'records': 0,
    'startingRecord': 0,
    'searchOptions':'1',
    'searchWithYourSignUpLanguage':'English', 
  }
}

r = requests.post('https://api.mouser.com/api/v1/search/keyword?apiKey=cf621336-fea9-4734-81dd-a8442ed3e05c', headers=headers, data=data)
print(r.status_code)
dataout = r.json()
print(dataout)


