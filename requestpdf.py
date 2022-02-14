from pathlib import Path
import requests 
import getpass 
username = getpass.getuser()
#url = 'https://www.ti.com/lit/ds/symlink/drv8323.pdf?ts=1644838924353&ref_url=https%253A%252F%252Fwww.google.com%252F'
#url = 'https://www.mouser.com/datasheet/2/256/TMC4361A_LA_datasheet_Rev1_24-1878611.pdf'
url = 'https://www.mouser.com/datasheet/2/389/aek_mot_2dc40y1-1919662.pdf' 
filename = Path('metadata.pdf')
r = requests.get(url)
print(r)
filename.write_bytes(r.content) 


