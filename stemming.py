# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 17:19:13 2018

@author: naren
"""

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

#words = ["like","likely","liked","likes","liking"]
text = "You are vey likely to get liked by someone you like because the liking for each other is the reason for those likes"
words = word_tokenize(text)
for w in words:
    print(ps.stem(w),end=' ')