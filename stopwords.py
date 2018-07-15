# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 16:53:58 2018

@author: naren
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#To show the list of stopwords:
#set(stopwords.words('english'))
 
text = "It lays down the framework defining fundamental political principles,\
        establishes the structure, procedures, powers \
        and duties of government institutions and sets out fundamental rights, \
        directive principles and the duties of citizens. "
 
stop_words = set(stopwords.words('english'))
 
word_tokens = word_tokenize(text)
 
filtered_sentence = [w for w in word_tokens if not w in stop_words]
  
print(word_tokens)
print(filtered_sentence)

