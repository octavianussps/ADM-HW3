
from bs4 import BeautifulSoup
import requests
from collector_utils import PLOT, INTRO, DICT_INFOBOX, EMPTY_INFOBOX
import time
import pandas as pd
import numpy as np
import csv

#ConnectionError




# We are reading the HTML with all the page of wikipedia
list_of_pages = 'https://raw.githubusercontent.com/CriMenghini/ADM/master/2019/Homework_3/data/movies1.html'
request = requests.get(list_of_pages )


# we parse 
soup = BeautifulSoup(request.text, 'html.parser')

# we create a list with all the links
wiki_links = soup.select('a')
#print(len(wiki_links))
#print(cane(15))


possible_plots = ['#Plot','#Plot_summary', '#Premise']
                 
infos = ['title', 'intro', 'plot' ,'film_name', 'director', 'producer', 'writer', 'starring', 'music', 'release date', 'runtime', 'country', 'language', 'budget']
Name = ['Directed by', 'Produced by', 'Written by', 'Starring', 'Music by', 'Release date', 'Running time', 'Country', 'Language', 'Budget']


#print(wiki_links[:9])
N = 150
i = 0
while i < N:#len(wiki_links):
    print(i,str(i))
#for link in wiki_links[N: N + 10]:
    
    # open the wiki page
    link_i = requests.get(wiki_links[i].get('href'))
    soup_i = BeautifulSoup(link_i.content, 'html5lib')
    
    # read all the paragraph
    all_p_i = soup_i.find_all('p')
    
    # select inside <span> the tag Plot everything inside <h2> 
    #print(wiki_links[i].get('href'))
    no_plot = 0
    for k in possible_plots:
        try:
            tag_i = soup_i.select_one(k).find_parent('h2').find_next_sibling()
            plot = PLOT(tag_i, [])
            no_plot = 1
            break                         
        except:
            pass
    if no_plot == 0:
        plot = 'NA' 
            
    intro = INTRO(all_p_i,plot[0],[])    
    
    try: 
        table = soup_i.find('table', class_='infobox vevent')
        result = DICT_INFOBOX(soup_i,{})
    except:
        result = EMPTY_INFOBOX()
    
    
    
    InfoBox = [0]*14
    
    for k in range(10):
        InfoBox[k+4] = result.get(Name[k], 'NA')
    
    InfoBox[0] = soup_i.title.text[:-12]
    try:
        InfoBox[3] = table.find_all('tr')[0].text
    except:
        InfoBox[3] = ['NA']
    InfoBox[2] = ' '.join(plot)
    InfoBox[1] = ' '.join(intro)
    
    with open('./TSV/article_' + str(i) + '.tsv', 'wt') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow(InfoBox)
        
    
    time.sleep(np.random.randint(1, 6))
    i += 1



