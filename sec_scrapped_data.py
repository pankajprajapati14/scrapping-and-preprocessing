
# coding: utf-8

# In[6]:

from bs4 import BeautifulSoup
import requests
import re
 
filename = "get_details.csv"
 
file1=open(filename, "w")
 
url="https://www.sec.gov/foia/iareports/inva-archive.htm"
r=requests.get(url)
soup = BeautifulSoup(r.content, "lxml")
 
first_half = "https://www.sec.gov"
 
links = soup.find('div', {'id' : 'main-content'}).find_all('ul')
# from here I can get access to all the urls in the main-content div
 
'''
Each link has two <a> tags>. 1 for url ... 2 for
url format
https://www.sec.gov/foia/iareports/ia050117.zip
'''
 
file1.write('File_URL' + ',')
file1.write('Date' + ',')
file1.write('type' + '\n')
 
for item in links:
              item1 = item.find_all('li')
 
              for item2 in item1:
                           item3 = len(item2.find_all('a'))
                           #print(len(item3))
                           #get_len = len(str(item2.find_all('a')))
                           #print(get_len)
                          
                           if item3 == 2:
                                         type1 = "Exempt"
                                         #print("if mein hai")
                                         zip_url = item2.find('a')['href'] 
                                         comp_zip_url = first_half + zip_url
 
                                         date1 = re.findall(r"\D(\d{6})\D", comp_zip_url)[0]
    
                                         #print(y)
                                         file1.write(comp_zip_url + ',')
                                         file1.write(str(date1) + ',')
                                         file1.write(type1 + '\n')
 
                           else:
                                         type1 = "Non-Exempt"
                                         #print("else mein hai")
                                         zip_url = item2.find('a')['href'] 
                                         comp_zip_url = first_half + zip_url
                                         date1 = re.findall(r"\D(\d{6})\D", comp_zip_url)[0]
                                         file1.write(comp_zip_url + ',')
                                         file1.write(str(date1) + ',')
                                         file1.write(type1 + '\n')
 
file1.close()


# In[ ]:




# In[ ]:



