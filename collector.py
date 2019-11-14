from bs4 import BeautifulSoup
import requests
import time
import urllib.request, urllib.error, urllib.parse
import os.path
from collector_utils import PRINT
import json
#ConnectionError

# where we want save all the html files
save_path = '/home/lex/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/HTML'

#number_link_title = {}

# counter for the name of the file
counter = 0#20530#5010

# A loop for each list of link
for i in range(1,4):
    
    # We are reading the HTML with all the links for the pages of wikipedia
    list_of_pages = 'https://raw.githubusercontent.com/CriMenghini/ADM/master/2019/Homework_3/data/movies' + str(i) + '.html'               
    request = requests.get(list_of_pages )
    
    
    # we parse this file 
    soup = BeautifulSoup(request.text, 'html.parser')
    
    # we create a list with all the links
    wiki_links = soup.select('a')
    
    N = len(wiki_links)
    for j in range(0,N):
        try:
            print(i,j,counter)
            # read the j-th page of wikipedia in the i-th HTML page of all links
            response = urllib.request.urlopen(wiki_links[j].get('href'))
            webContent = response.read().decode(response.headers.get_content_charset())
            
            # this function save this page in an .html file inside the folder at the address save_path 
            PRINT(save_path, counter, webContent)
            soup_i = BeautifulSoup(webContent, 'html5lib')
            #a = soup_i.title.text[:-12]
            #number_link_title[counter] = (soup_i.title.text[:-12], wiki_links[j].get('href'))
            
        #except 'error409':
        #    time.sleep(1200)
        except:
            PRINT(save_path, counter, 'NA')
            
            pass
        counter += 1
        time.sleep(0.01)










