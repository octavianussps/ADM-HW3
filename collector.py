from bs4 import BeautifulSoup
import requests
import time
import urllib.request, urllib.error, urllib.parse
import os.path
from collector_utils import PRINT

#ConnectionError

# where we want save all the html files
save_path = '/home/lex/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/HTML'


# counter for the name of the file
counter = 19994

# A loop for each list of link
for i in range(3,4):
    
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
            webContent = response.read()
            
            # this function save this page in an .html file inside the folder at the address save_path 
            PRINT(save_path, counter, webContent)
            counter += 1
        #except 'error409':
        #    time.sleep(1200)
        except:
            pass
        time.sleep(0.01)



'''

import urllib.request
 
url= 'https://asd.com/asdID='
for i in range(1, 5):
    print('     --> ID:', i)
    newurl = url + str(i)
    f = open(str(i)+'.html', 'w')
    page = urllib.request.urlopen(wiki_links[i].get('href'))
    pagetext = str(page.read())
    f.write(pagetext)
    f.close()
    
    
    
    
    
#fid=urllib.request.urlopen(link_i)
fid = urllib.request.urlopen(wiki_links[i].get('href'))
fi = fid.read()
webpage=fid.read().decode('utf-8')



save_path = '/home/lex/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/HTML'

name_of_file = 'article_' + str(i) + '.html'

completeName = os.path.join(save_path, name_of_file)
with open(completeName, 'w') as out_file:
    out_file.write('please')


'''









