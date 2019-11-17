# ADM-HW3
This Repositor holds the detials structure for building a search engine over a list of movies that have a dedicated page on Wikipedia.
along with an algorithm question related to Longest palandromic Subsequence of a string

The repository is driven in a way to first of all collect data, parse the information, creaing index approach to implement dictionary and vocabulary. Then to create conjuntive quey for a search Engine to locate the information from our collected Data, This repository is based on 6 major Steps.

A) Data collection

B) Data Parsing

C) Indexing/Invert Indexing

D) Search Engine - Query Executing

E) Algorithm for Longest Palandromic Subsequence


## Data Collection

Data is extracted from three HTML files containing 10,000 Wikipedia links each file that is related to Movies. we have used Beautiful library for HTML parsing of HTML File and extracting links from the HTML File.

On the second phase we obtain the data from each link and save it as an HTML file in a folder.

The above explanation is linked to the Collector.py and Collector_utils.py files available in Library, where Collector_Utils conatins the function for Collector.py

## Data parsing

Here we read and HTML files and extracted the INTRO PLOT and INFO_Box Data and save it into a TSV file.

1.Reading from HTML Folder HTML Files

2.Extracting the Required data via fetching the function from PARSING_UTILS

3.making TSV Output in a TSV folder

The above explanation is linked with the files PARSER.py and PARSER_UTILS.py available in the repository.

## Indexing/Invert Indexing

firstly cleaning of data with nltk library

Created Direct Index- Dictionary where WORD is a KEY, and value is the another dictionary with a key NUMBER OF DOCUMENT and Value THE FREQUENCY OF WORD in this Document

Created INVERTED index for the same

Combining all these function in INDEX_UTILS.py available in Repository

by using above function created 3 dictionaries INVERTED_INDEX.pkl | VOCABLUARY.pkl | LENGTH_DOC.pkl

The above information is availble in INDEX.py and INDEX_UTILS.py files in repository

## Search Engine - Query Executing

#### Conjunctive Query

For the conjunctive query we see only the number of documents in the Inverted_index dictionary, save for each word a vector with these numbers and after matking the AND of these vectors

The above information is coded in the main.py available in repository.


### Cosine similarity

we calculated the tfidf for the query and executed the cosine similary with the documents obtained from the conjuntive query.

#### Our Score

The user can also decide the number of links to see, he can also specify the director and the composer.

The score is based on the word frequency in documents that contain all the words in the query. 
The score is the mean of the frequencies.

If the composer or director matches whit the choose of the user, the score of the document will be increased by 25%.

## Algorithm for Longest Palandromic Subsequence

### Answer: 

The Idea that is referred in this question is of the longest palindromic subsequence. I am defining this algorithm with the dynamic programming approach which is defined as dividing a problem into sub-problems, then solving these sub-problems in a way to store their results in a structure dataset for future query.
First of all understand the problem, let’s suppose the sequence is “anwaralam” and its length is 9 and index 0-8. So,

1.	First part is to identify the subsequences of this sequence, which can be defined as the sub-problem of the main - - problem.

2.	Then second part is to identify their palindromic nature from first and last element of the subsequence and store the result in a data structure, (data structure is defined as a 2 dimensional table DST in our case)

3.	Thirdly to identify the longest Palindromic Subsequence from the data structure of stored result.

Detail Answer with algorithm Explataion is available in Answer_Algorithm_Question4.md and Coding is available in exercie4.py

<p align="left">
<img src="https://github.com/anwaralamgithub/ADM2019HW3_Movies_Search_Engine/blob/images/FIG5.jpg" height=430 
</p>

________________________________________________________________________________________________________________________
<p align="left">
<img src="https://github.com/anwaralamgithub/ADM2019HW3_Movies_Search_Engine/blob/images/FIG6.jpg" height=430 
</p>




