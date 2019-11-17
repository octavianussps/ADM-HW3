

import numpy as np
from index_utils import FILTER
import pickle
from functools import reduce
import pandas as pd
    



file = '/home/lex/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/'
with open(file + 'Inverted_index.pkl', 'rb') as fp:
    Inverted_index = pickle.load(fp)

with open(file + 'Vocabulary.pkl', 'rb') as fp:
    Vocabulary = pickle.load(fp)

with open(file + 'Doc_Id_url.pkl', 'rb') as fp:
    Doc_Id_url = pickle.load(fp)


Query = 'disney movie 2019\n'

Query = FILTER(Query) 
All_docs = []



Docs = []
for i in Query:
    Docs.append(np.fromiter(Inverted_index[Vocabulary[i]].keys(), dtype=int))
    #Docs.append(np.array(Inverted_index[Vocabulary[i]].keys()))
    Films = reduce(np.intersect1d, Docs)
    





####
    #create a dictionary with links and number in Collectro.py
    #generate a dataframe
    # reupload index and index_utils collector parse




