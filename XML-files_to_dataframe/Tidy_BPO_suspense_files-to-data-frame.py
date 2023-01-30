#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import 
import os
import pandas as pd
import regex as re
from pathlib import Path
from collections import Counter


# In[2]:


# Generate a corpus by loading all the BPO xml files from the chosen directory 
# and list the names of the first 10 xml files 
corpus = os.listdir('suspense/')
corpus[:10]


# In[3]:


# Print how many xml files are in the corpus
corpus_length = len(corpus)
print(corpus_length)


# In[4]:


# Create an empty dictionary for preparation of the conversion of the xml-file-corpus to a data frame
empty_dictionary = {}

# Loop through the folder of documents to open and read each one
for document in corpus:
    with open('suspense/' + document, 'r', encoding = 'utf-8') as to_open:
         empty_dictionary[document] = to_open.read()

# Populate the data frame with two columns: file name and document text
suspense_texts = (pd.DataFrame.from_dict(empty_dictionary, 
                                       orient = 'index')
                .reset_index().rename(index = str, 
                                      columns = {'index': 'file_name', 0: 'document_text'}))


# In[5]:


# show the first 10 lines of the data frame
suspense_texts[:10]


# In[6]:


# controll that the number of lines with text in the data frame equals the number of files in the folder
df_length = len(suspense_texts)
print(df_length)
corpus_length == df_length


# In[7]:


# Create a new column 'suspense' to store the frequency of the word 'suspense'for each text
suspense_texts['suspense_frequ'] = suspense_texts['document_text'].str.count('suspense')
# show the first 10 lines of the data frame
suspense_texts[:10]


# In[8]:


# use a reg ex to clean the document text from certain noisy wrong OCR 
suspense_texts['clean_text'] = suspense_texts['document_text'].str.replace("&amp;amp;","")
suspense_texts['clean_text'] = suspense_texts['clean_text'].str.replace("&amp;quot;","")
suspense_texts['clean_text'] = suspense_texts['clean_text'].str.replace("&amp;apos;","")
suspense_texts['clean_text'] = suspense_texts['clean_text'].str.replace("&apos;","")


# In[ ]:


# show the first 10 lines of the data frame
suspense_texts[:10]


# In[20]:


# optional: to controll if every file/line contains xml-tags or one chosen xml-tag, see regular expression

#suspense_texts['suspense_Title_frequ'] = suspense_texts['document_text'].str.count('</Title>')

# optional: to filter for files/lines containing xml-tags
#suspense_title_once = suspense_texts[suspense_texts['suspense_Title_frequ'] == 1]

# optional: controll if there is no file with </Title> more or less than 1 time
#xml-tagged-file_length = len(suspense_title_once)
#xml-tagged-file_length == df_length


# In[10]:


# Show the column names of the current state of the data frame
suspense_texts.columns


# In[42]:


# optional: to delete a column of a data frame --> if you added a column by accident

#del suspense_texts['suspense_periodical_titel']


# In[11]:


# optional: try different regular expressions to extract content from inbetween xml-tags
# with the given xml-tag you extract the titles of the periodicals in the corpus
suspense_texts['document_text'].str.extract(r'(<Title>((.)*)</Title>)')#[1]
# use the index [1] to extract only the one column that contains the content between the xml-tags and not the column with indicated xml-tags


# In[12]:


# use a reg ex to extract the content between the chosen xml-tags. save the index [1] column only to the data frame
suspense_texts['suspense_journal_title'] = suspense_texts['document_text'].str.extract(r'(<Title>((.)*)</Title>)')[1]
 


# In[13]:


# use a reg ex to extract the publication date and store it in a new column of the dataframe
suspense_texts['suspense_journal_date'] = suspense_texts['document_text'].str.extract(r'(<AlphaPubDate>((.)*)</AlphaPubDate>)')[1]


# In[14]:


# use a reg ex to extract the pure file text without the xml-tags and metadata
suspense_texts['pure_text'] = suspense_texts['clean_text'].str.extract(r'(<FullText>((.)*)</FullText>)')[1]


# In[15]:


# show the cleaned text for controll
suspense_texts['pure_text'][:20]


# In[16]:


# show the first 10 lines of the data frame
suspense_texts[:10]


# In[28]:


# use reg ex to extract the publication year only of the indicated publication date that can include day and month as additional metadata 
# indicate that the extracted year is stored as type: integer for the following steps
suspense_texts['suspense_journal_year'] = suspense_texts['suspense_journal_date'].str.extract(r'(\d{4})')
suspense_texts['suspense_journal_year'] = suspense_texts['suspense_journal_year'].astype(int) 
print(type(suspense_texts['suspense_journal_year']))


# In[27]:


# optional: show and controll the current state of the dataframe before you store it in a csv-file in the next step
#suspense_texts[:15]


# In[19]:


# store the dataframe in a new directory
filepath = Path('select/out_all_bpo_texts_as_df.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
suspense_texts.to_csv(filepath) 


# Here starts the filtering of all bpo files to get only those interesting to our case study.

# In[20]:


# build a subset out of all the documents that contain the word "suspense" at least 2 times.
suspense_subset = suspense_texts[suspense_texts['suspense_frequ'] > 1]
suspense_subset[:10]


# In[21]:


# show the number of files containing the word "suspense" ≤ 2 times.
len(suspense_subset)
# 368 of the 2635 documents contain the word "suspense" ≤ 2 times.


# In[22]:


#print the column names of the subset
suspense_subset.columns


# In[29]:


# create a new subset of "suspense"-containing texts by filtering by the year of publication between 1800 and 1900.
suspense_19_subset = suspense_texts[(suspense_texts['suspense_journal_year'] > 1799) & (suspense_texts['suspense_journal_year'] < 1901) & (suspense_texts['suspense_frequ'] > 1)]
# this is a 19th century subset of bpo files that contain the word "suspense" at least 2 times.


# In[30]:


# show and controll the current state of the dataframe before you store it in a csv-file in the next step
suspense_19_subset[:10]


# In[31]:


# show the number of files in the 19th century subset of bpo files that contain the word "suspense" at least 2 times
len(suspense_19_subset)
# 313 of the 368 "suspense"-containing files contain the word "suspense" ≤ 2 times and are taken from 19th century periodicals.


# In[32]:


# store the subset of the dataframe in a new directory
filepath = Path('select/out_all_suspense_texts_19.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
suspense_19_subset.to_csv(filepath) 


# In[151]:


# optional: indicate if the words "Dublin" or "Edinburgh" are part of the title of a periodical.
suspense_texts['suspense_journal_title'].str.match('Dublin' or 'Edinburgh')


# In[34]:


# create a new subset of "suspense"-containing texts by filtering by the year of publication between 1800 and 1900 and excluding periodicals from Edinburgh and Dublin to get an English only corpus.
suspense_19_Eng_subset = suspense_texts[(suspense_texts['suspense_journal_year'] > 1799) & (suspense_texts['suspense_journal_year'] < 1901) & (suspense_texts['suspense_frequ'] > 1) & (suspense_texts['suspense_journal_title'].str.match('Dublin' or 'Edinburgh') == False)]


# In[35]:


# show and controll the current state of the dataframe before you store it in a csv-file in the next step
suspense_19_Eng_subset[:10]


# In[157]:


# store the subset of the dataframe in a new directory
filepath = Path('select/out_all_suspense_texts_19_Eng.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
suspense_19_Eng_subset.to_csv(filepath) 
# "suspense" min. 2 times, English only by excluding "Dublin" & "Edinburgh", 19th century only
#end of the notebook

