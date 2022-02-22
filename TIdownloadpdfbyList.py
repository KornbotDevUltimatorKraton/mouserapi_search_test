import datetime as dt
import shutil
import time
from selenium import webdriver
from mechanize import Browser
from selenium import *
from selenium.webdriver.chrome.options import Options
from __future__ import print_function



# TI download pdf by part list  

options = Options()
# location ให้ save pdf (ต้องแก้ถ้าใช้ linux)
downloadedloc=r"F:\chromedriver_win32"

# ++++ download https://chromedriver.chromium.org/downloads ก่อน และเลือกให้ตรง version
driverloc=r"F:\chromedriver_win32\chromedriver.exe"
pdfBase_url = f"https://www.ti.com/lit/ds/symlink/"


######  start :: Edit here #####
part_list=["TMAG5170","BQ25180","BQ25180","BQ25672"]
ext = f".pdf"
######  end :: Edit here #####


pdf_url_list =  list(map(lambda x:pdfBase_url+x.lower()+ext, part_list))

#options.add_argument('--headless') # comment to see how it works
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')
options.add_argument('--incognito')
options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
options.add_experimental_option("prefs", {
"plugins.plugins_list": [{"enabled": False, 
"name": "Chrome PDF Viewer"}],
"download.default_directory" : downloadedloc,
"download.prompt_for_download": False,
"download.directory_upgrade": True,
"safebrowsing_for_trusted_sources_enabled": False,
"safebrowsing.enabled": True,
"detach": True,
"excludeSwitches": ["enable-automation"],
'useAutomationExtension': False,
"plugins.always_open_pdf_externally": True

})       
driver = webdriver.Chrome(( driverloc ) , options=options)

list(map(print, pdf_url_list[:3])) 

for _pdf in pdf_url_list:
    try:
        driver.get(_pdf)
        time.sleep(3)
    except Exception as e:
        # if maximam exceed, click some link above 
        print(_pdf)
        print(e)
        
driver.quit()