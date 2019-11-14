from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from collections import Counter
import numpy as np


stopWords = set(stopwords.words('english'))


def FILTER(string):
    string = string.lower()
    tokenizer = RegexpTokenizer("[\w']+")
    Intro_Plot = tokenizer.tokenize(string)
    wordsFiltered = []
    for w in Intro_Plot:
        if w not in stopWords:
            wordsFiltered.append(w)
    porter = PorterStemmer()
    ListOfWords = [porter.stem(word) for word in wordsFiltered]
    return ListOfWords


def DOC_DOCLEN_FREQ(Document, direct_index, i):
    Length = len(Document)
    Document = Counter(Document)
    for word, frequence in Document.items():
        if word not in direct_index:
            direct_index[word] = [(i, Length, frequence)]
        else:
            direct_index[word].append((i, Length, frequence))
    return 

def INVERTED_INDEX(direct_index, Inverted_index, N):
    for key, Items in direct_index.items():
        Inverted_index[key] = []
        for item in Items:
            Inverted_index[key].append((item[0], (item[2]/item[1])*np.log(N/len(Items))))
    return 





# text = text.replace("'", "")