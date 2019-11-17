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




