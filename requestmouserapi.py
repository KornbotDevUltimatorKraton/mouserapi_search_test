import json 
import urllib.request
from urllib import request
import requests
from requests.structures import CaseInsensitiveDict
import getpass 
username = getpass.getuser() 
curl = 'curl -X POST "https://api.mouser.com/api/v1/search/partnumber?apiKey=cf621336-fea9-4734-81dd-a8442ed3e05c" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"SearchByPartRequest\": { \"mouserPartNumber\": \"LM324\", \"partSearchOptions\": \"1\" }}"'
curl1 = 'curl -X POST "https://api.mouser.com/api/v1/search/keyword?apiKey=cf621336-fea9-4734-81dd-a8442ed3e05c" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"SearchByKeywordRequest\": { \"keyword\": \"DC motor driver IC\", \"records\": 0, \"startingRecord\": 0, \"searchOptions\": \"1\", \"searchWithYourSignUpLanguage\": \"English\" }}"'
headers = CaseInsensitiveDict()
headers["acccept"] = "application/json"
headers["Content-Type"] = "application/json"

data = { 

  'SearchByKeywordRequest': {
    'keyword': 'DC motor driver IC',
    'records': 0,
    'startingRecord': 0,
    'searchOptions':1,
    'searchWithYourSignUpLanguage':'English', 
  }
}
r = requests.post('https://api.mouser.com/api/v1/search/keyword?apiKey=cf621336-fea9-4734-81dd-a8442ed3e05c', headers=headers, json=data)
print(r.status_code)
dataout = r.json()
print(dataout)
print(headers)
print(list(dataout))
datajson = dataout.get(list(dataout)[1])
print(list(datajson))
print(datajson.get(list(datajson)[1]))
getpart = datajson.get(list(datajson)[1]) 
pathpdf = "/home/"+username+"/"+"Parts_pdf/"
def downloadpdf(pdflink,filename):
        response = urllib.request.urlopen(pdflink) 
        file = open(pathpdf+filename+'.pdf','wb') 
        file.write(response.read()) 
        file.close() 

for j in list(getpart): 
       Link_Data = j.get('DataSheetUrl')
       print("File name: ",Link_Data,j.get('DataSheetUrl').split('/')[len(j.get('DataSheetUrl').split('/'))-1])
       filename = j.get('DataSheetUrl').split('/')[len(j.get('DataSheetUrl').split('/'))-1]
       #downloadpdf(Link_Data,filename) 
