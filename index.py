
import os.path
from index_utils import FILTER, DOC_DOCLEN_FREQ, INVERTED_INDEX
from collections import Counter
import numpy as np
import os.path
from collector_utils import PRINT
import json
import pickle

output_path = '/home/lex/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/TSV'
direct_index = {}
Inverted_index_words = {}
Inverted_index = {}
Vocabulary = {}

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
    
        
    DOC_DOCLEN_FREQ(Document, direct_index, i)
    
    
    
    i += 1
        
INVERTED_INDEX(direct_index, Inverted_index_words, N)

counter = 0
for i,j in Inverted_index_words.items():
    Vocabulary[i] = counter
    Inverted_index[counter] = j
    counter += 1

    
file = '/home/lex/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/Inverted_index'



with open(file+'.json', 'w') as fp:
    json.dump(Inverted_index, fp)

with open(file+'.json', 'r') as fp:
    da = json.load(fp)


with open(file+'.pkl', 'wb') as fp:
    pickle.dump(da, fp, protocol = pickle.HIGHEST_PROTOCOL)

with open(file+'.pkl', 'r') as fp:
    dat = pickle.load(fp)

with open(file + '.txt', 'w') as fp:
    fp.write(str(da))

import sys




