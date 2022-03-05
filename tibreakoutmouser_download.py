from re import search
import os 
import bs4 # Getting the beautiful soup request data 
import json 
import urllib.request
from urllib import request
import requests
from requests.structures import CaseInsensitiveDict
import getpass 
from pathlib import Path

username = getpass.getuser() 
#curl = 'curl -X POST "https://api.mouser.com/api/v1/search/partnumber?apiKey=cf621336-fea9-4734-81dd-a8442ed3e05c" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"SearchByPartRequest\": { \"mouserPartNumber\": \"LM324\", \"partSearchOptions\": \"1\" }}"'
#curl1 = 'curl -X POST "https://api.mouser.com/api/v1/search/keyword?apiKey=cf621336-fea9-4734-81dd-a8442ed3e05c" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"SearchByKeywordRequest\": { \"keyword\": \"DC motor driver IC\", \"records\": 0, \"startingRecord\": 0, \"searchOptions\": \"1\", \"searchWithYourSignUpLanguage\": \"English\" }}"'

mode = 0o777 # Getting permission create the directory 
HOME_PATH = "/home/"+username+"/Automaticsoftware/" # Gettig the home path to point the file downloaded into the list 
Document = HOME_PATH+"Downloadedpackage/"   # Manage the directory to download the file into the path 
try:
   os.mkdir(Document) #Create the document 
except: 
   pass
CONFIG   = "/home/"+username+"/Automaticsoftware/Configuresearch" # Config file
headers = CaseInsensitiveDict()
headers["acccept"] = "application/json"
headers["Content-Type"] = "application/json"
category_manage = {}
Write_category_mem = {}
#Insert requirement inside the data json here for search capabiity 
key_words = "Texas instrument  i2c multiplexer ic"
all_lowercase = key_words.islower()
convert_lowercase = "" 
if all_lowercase == False: 
        convert_lowercase = key_words.lower()  
configure_search = {'motor':"Motor/Motion/Ignition Controllers & Drivers"} 
list_config = os.listdir(CONFIG)
config= list_config[0] #Select the config file in the list of the directory 
Data_package_name = {} 
#Finding the intersection of the list 
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3   


data = { 

  'SearchByKeywordRequest': {
    'keyword': key_words,
    'records': 0,
    'startingRecord': 0,
    'searchOptions':1,
    'searchWithYourSignUpLanguage':'English', 
  }
}
r = requests.post('https://api.mouser.com/api/v1/search/keyword?apiKey=cf621336-fea9-4734-81dd-a8442ed3e05c', headers=headers, json=data)
print(r.status_code)
dataout = r.json()
#print(dataout)
#print(headers)
#print(list(dataout)[1])
def Configure(configfile): 
     try: 
       data = open(CONFIG+"/"+str(configfile),'r') #Open the configuretion file for the path 
       datas = data.readline()
       transfer = json.loads(datas)
       return transfer
     except:
        print("Not found the configure file please check again")
config_data = Configure(config)
def Getpackage_all_link(dataout,config_data):
      for ig in list(dataout): 
        try:
            print("header list",ig)
            datajson = dataout.get(list(dataout)[1])
            #print(datajson)
            #print(list(datajson))
            #print(datajson.get(list(datajson)[1]))
            getpart = datajson.get(list(datajson)[1]) 
            #print('getpart',getpart)
            print(list(getpart)[0])
        except: 
            print("Out of range")
     
      for ij in range(0,len(list(getpart))): 
                 Product_info = list(list(getpart)[ij]) 
                 #for rt in range(0,len(Product_info)): 
                 #print(list(getpart)[ij].get(Product_info[2]))
                 print(list(getpart)[ij].get(Product_info[16]),list(getpart)[ij].get(Product_info[5])) 
                 category_manage[list(getpart)[ij].get(Product_info[5])+"_"+str(ij)] = list(getpart)[ij].get(Product_info[16])
                 Write_category_mem[list(getpart)[ij].get(Product_info[5])] = ij

      print(category_manage)
      print("Category data",list(Write_category_mem))

      #Generate the category data inside the list 
      jsonstring = json.dumps(Write_category_mem) 
      components_write = open("category_components.json",'w')
      #Writing the json file into the home path directory to running the api data
      components_write.write(jsonstring)  
      components_write.close()     
      for ir in range(0,len(category_manage)):
           components = category_manage.get(list(category_manage)[ir])
           Manufacturer = components.split("https://")[1].split("/")[2]
           compackage = components.split("https://")[1].split("/")[3].split("?")[0] 
           drawing_pack = config_data.get('package').get('packagesdrawing')
           #replace and remove drawing package from the list 
           for re in range(0,len(drawing_pack)): 
                  try:
            
                    if search(drawing_pack[re],str(compackage)):
                      output_package = compackage.replace(str(drawing_pack[re]),"",1) 
                      #print(output_package)
                      Data_package_name[output_package] = drawing_pack[re] 
                      #print(output_package,drawing_pack[re])
                      print("Found drawing pakage",output_package,drawing_pack[re])

                  except:
                      pass  
      
      return Data_package_name

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Processing the data of the category extraction 
Pack_drawing_json = Getpackage_all_link(dataout,config_data)
print(Pack_drawing_json)
def Google_search_package(Pack_drawing_json): 

      for p in list(Pack_drawing_json):   
              
              text= p.lower()  #insert the search data here 
              print(text)
              url = 'https://google.com/search?q=' + text  #Select google as search engine 

              check_menufac = ['ti','nxp','st']
              # Fetch the URL data using requests.get(url),
              # store it in a variable, request_result.
              request_result=requests.get(url)
              # Creating soup from the fetched request
              soup = bs4.BeautifulSoup(request_result.text,"html.parser")
              #print(soup)
              #print(type(soup))
              for a in soup.find_all('a', href=True):
                       #print("Found the URL:", a['href'])
                       try:
                           if len(a['href'].split('/url?q=')) == 2:
                                  print("Manufacturer",a['href'].split('/url?q=')[1].split('&')[0].split("https://")[1].split("/")[0].split(".")[1])
                                  data_link_menufac = a['href'].split('/url?q=')[1].split('&')[0].split("https://")[1].split("/")[0].split(".")[1]
                                  if data_link_menufac in check_menufac[0]:
                                      try:
                                                  print(a['href'].split('/url?q=')[1].split('&')[0])
                                                  length = len(a['href'].split('/url?q=')[1].split('&')[0].split("/")) -1
                                                  url_link = a['href'].split('/url?q=')[1].split('&')[0].split("/")[length]
                              
                                                  #Making download hear 
                                                  url = 'https://www.ti.com/lit/ds/symlink/'+url_link+".pdf" 
                                                  getname = url.split(".pdf")[0].split("/")[len(url.split(".pdf")[0].split("/"))-1]
                                                  print(getname)
                                                  filename = Path(Document+text+'.pdf')
                                                  r = requests.get(url)
                                                  if int(r.status_code) == 200:
                                                         print(r.status_code) 
                                                         filename.write_bytes(r.content) 
                                                         
                                                         break 
                                      except: 
                                          print("Out of range data match")
                                                                        
                       except:
                            pass
#Running the function of search algorithm
Google_search_package(Pack_drawing_json)