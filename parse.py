
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import numpy as np
import csv
from parse_utils import PLOT, INTRO, DICT_INFOBOX, EMPTY_INFOBOX
import os.path
#ConnectionError




input_path = '/home/lex/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/HTML'
output_path = '/home/lex/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/TSV'

possible_plots = ['#Plot','#Plot_summary', '#Premise']
                 
infos = ['title', 'intro', 'plot' ,'film_name', 'director', 'producer', 'writer', 'starring', 'music', 'release date', 'runtime', 'country', 'language', 'budget']
Name = ['Directed by', 'Produced by', 'Written by', 'Starring', 'Music by', 'Release date', 'Running time', 'Country', 'Language', 'Budget']


#print(wiki_links[:9])
N = 29982
i = 19994
while i < N:#len(wiki_links):
    print(i,str(i))
#for link in wiki_links[N: N + 10]:
    completeName_input = os.path.join(input_path, 'article_' + str(i) + '.html')
    with open(completeName_input, 'r') as out_file:
        page = out_file.read() 
    
    soup_i = BeautifulSoup(page, 'html5lib')
    
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
        InfoBox[3] = 'NA'
    InfoBox[2] = ' '.join(plot)
    InfoBox[1] = ' '.join(intro)
    
    completeName_output = os.path.join(output_path, 'article_' + str(i) + '.tsv')
    with open(completeName_output, 'wt') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow(InfoBox)
        
    
    
    i += 1


'''
import os.path

save_path = '/home/lex/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/HTML'

completeName = os.path.join(save_path, 'article_' + str(8) + '.html')
with open(completeName, 'r') as out_file:
    a = out_file.read()

'''














