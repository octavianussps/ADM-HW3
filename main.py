

import numpy as np
from index_utils import FILTER
import pickle
from functools import reduce
import pandas as pd
import os.path



def conjuntive_query(Query, Inverted_index, Vocabulary, Docs):
    for i in Query:
        # select all the docs with a specific word and appen this array to another array
        Docs.append(np.fromiter(Inverted_index[Vocabulary[i]].keys(), dtype=int))
    # make the and
    Films = reduce(np.intersect1d, Docs)
    return Films



def output_conjuntive_query(Films, input_path):
    Title = []
    Intro = []
    Url = []
    # for each film selected we are going to save title, intro and url
    for i in Films:
        completeName_input = os.path.join(input_path, 'article_' + str(i) + '.tsv')
        with open(completeName_input, 'r') as input_file:
            document = input_file.readline()
        document= document.split('\t')
        Title.append(document[0])
        Intro.append(document[1])
        Url.append(Doc_Id_url[i])
        
    #create a dictionary
    Data = {'title' : Title,
            'intro' : Intro,
            'url' : Url
            }
    # make the dataframe 
    df = pd.DataFrame(data=Data)
    return df



# folder with the tsv files
input_path = '/home/lex/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/TSV'

# reading the dictionaries
file = '/home/lex/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/'
with open(file + 'Inverted_index.pkl', 'rb') as fp:
    Inverted_index = pickle.load(fp)

with open(file + 'Vocabulary.pkl', 'rb') as fp:
    Vocabulary = pickle.load(fp)

with open(file + 'Doc_Id_url.pkl', 'rb') as fp:
    Doc_Id_url = pickle.load(fp)



# input for the user
while True:
    try:
        Choice = int(input('which search: 1, 2 or 3?'))
        if Choice == 3:
            # maybe somthing as 'do you want specify the director?'
            pass
        else:
            Query = input('amazing: the query is?')
        break
    except:
        print('try again')

# filtering the query
Query = FILTER(Query) 

# initialize two arrays
All_docs = []
Docs = []




# if conjuntive query
if Choice == 1:
    # search all the rigth movies
    Films = conjuntive_query(Query, Inverted_index, Vocabulary, Docs)
    #make the dataframe
    df = output_conjuntive_query(Films, input_path)
    print(df)

if Choice == 2:
    pass

if Choice == 3:
    pass


'''

for i in Films:
    print(Doc_Id_url[i])
c=[]
for i in Vocabulary:
    c.append(i)    
'''

####
    #create a dictionary with links and number in Collectro.py
    #generate a dataframe
    # reupload index and index_utils collector parse




