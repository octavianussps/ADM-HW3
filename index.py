
import os.path
from index_utils import FILTER, DOC_DOCLEN_FREQ, INVERTED_INDEX
from collections import Counter
import numpy as np
import os.path
from collector_utils import PRINT
import json


output_path = '/home/lex/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/TSV'
Vocabolary = {}
Inverted_index = {}
N = 29982
i = 0
while i < N:#len(wiki_links):
    print(i,str(i))
    completeName_output = os.path.join(output_path, 'article_' + str(i) + '.tsv')
    with open(completeName_output, 'r') as input_file:
        intro_plot = input_file.readline()
    intro_plot = intro_plot.split('\t')[1:3]
    intro_plot = str(intro_plot[0]) + ' ' + str(intro_plot[1])
    
    Document = FILTER(intro_plot)
    
        
    DOC_DOCLEN_FREQ(Document, Vocabolary, i)
    
    
    
    i += 1
        
INVERTED_INDEX(Vocabolary, Inverted_index, N)
    
file = '/home/lex/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/Inverted_index.json'


with open(file, 'r') as fp:
    data = json.load(fp)
