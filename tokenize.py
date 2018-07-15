# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 14:25:18 2018

@author: naren
"""

from nltk.tokenize import sent_tokenize, word_tokenize

text = "The Constitution of India is the supreme law of India. \
        It lays down the framework defining fundamental political principles,\
        establishes the structure, procedures, powers \
        and duties of government institutions and sets out fundamental rights, \
        directive principles and the duties of citizens. \
        It is the longest written constitution of any sovereign country in the world."


print(sent_tokenize(text))

print(word_tokenize(text))