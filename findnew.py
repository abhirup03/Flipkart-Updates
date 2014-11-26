import requests
from bs4 import BeautifulSoup
import os
import time

os.system('clear')
out = []

while 1:
   page = requests.get("http://www.flipkart.com/")
   src = page.text
   ob = BeautifulSoup(src)

   for find,find2 in zip(ob.findAll('div',{'class':'offerSubTitle'}),ob.findAll('div',{'class':'offerTitle'})):
      title = find.text
      price = find2.text
      if title not in out:
         out.append(title)
      else:
         continue
      time.sleep(0.3)
      print title.strip() + " : " + price.strip()
   
   time.sleep(5)
