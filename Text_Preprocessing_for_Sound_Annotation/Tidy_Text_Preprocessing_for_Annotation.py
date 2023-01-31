#!/usr/bin/env python
# coding: utf-8

# This jupyter notebook is used for the preparation of plain text files (.txt) for the annotation in spread sheets. For that we read in a txt-file, make sure it's encoded in UTF-8, clean the text file for double white spaces (\s) and line breaks (\n) as well as further elements in the text that could disturb its tokenization and future xml conversion like: %, &, $.
# In a next step, it uses the NLTK Tokenizer for English (default) to tokenize the plain text file that can be saved in a facultative step. 

# In[1]:


import nltk
import regex as re
from nltk.tokenize import word_tokenize
from pathlib import Path
import pandas as pd


# In[2]:


# Read in the text file and make sure it's encoded in UTF-8. 
# Please change it to your respective file path.

text = open("/PATH/TO/plain_text_file.txt", mode='r', encoding='utf-8-sig').read()
text[:100]


# In[3]:


# Clean the text with some simple regex comands to substitute the double white spaces (\s) 
# and line breaks (\n) as well as further elements in the text that could disturb its tokenization 
# with single white space or characters of our choice.

single_spaces_text = re.sub('\s+', ' ', text)
single_spaces_text = re.sub('--+', ' -- ', text)
single_spaces_text = re.sub('&', 'and', text)
single_spaces_text = re.sub(';', '.', text)
single_spaces_text = re.sub('\d', ' ', text)
#print(single_spaces_msg)
no_space_text = re.sub('\n+', ' ', single_spaces_text)
print(no_space_text[:100])

# Check the type of your document.

type(no_space_text)


# In[4]:





# In[5]:


# Define the variable "tokens" in which you want to save the result of the NLTK tokenization process.

tokens = word_tokenize(no_space_text)
tokens[:10]

# Check the type of your tokenization. It should be a list of tokens.

type(tokens)


# In[262]:


# Facultative step:
# Create a new text file. Save the list of tokens in the text file.

#with open('../Wells_War_of_the_Worlds_tokenized.txt', 'w') as no_space_text:
#    for listitem in tokens:
#        no_space_text.write(f'{listitem}\n')


# In[8]:


# Take the NLTK WordNet Lemmatizer.
lmtzr = nltk.WordNetLemmatizer()


# In[9]:


# Lemmatize the token list "tokens" and store it in the variabel "token_lemma".
token_lemma = [lmtzr.lemmatize(token) for token in tokens]
#print(token_lemma[:100])


# In[10]:


# POS-tag the list of tokens and store the pos-tagged data in the variabel "tagged".
tagged = nltk.pos_tag(token_lemma)
print(tagged[:20])
len(tagged)


# In[13]:


# Generate a dataframe with the entries "lemma" and "pos" to store the data received from the NLTL-POS-tagging.
df = pd.DataFrame(tagged, columns=['lemma', 'pos'])
#df.head(n = 10)


# In[15]:


# Add a further column to your dataframe that contains the tokens generated earlier with the NLTK tokenizer.
df['token'] = tokens
df.head(n = 10)


# In[16]:


# Define the variable "length" with the calculated length of the list of tokens "tokens"
# and store it as an integer in the variable "length".
# Then generate a new column of "O" that are the "not-annotated" annotation entries of the dataframe of the length of the list of tokens. 

length = len(tokens)
print(length)
list = ['O']* length 
#len(list)


# In[18]:


# Show and controll the data frame before saving it to a csv-file.
df['annotation'] = list
df.head(n = 10)


# In[ ]:


# Save the dataframe to a csv-file.
filepath = Path('/PATH/TO/text_file_for_annotation.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
df.to_csv(filepath)

