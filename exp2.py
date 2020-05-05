# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:50:10 2020

@author: rajmugdha
"""


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text="Nick likes to play football, however he is not too fond of tennis"
stopwords=list(stopwords.words('english'))
words=word_tokenize(text)
filtered_text=[w for w in words if not w in stopwords]
print("original sentence:"+text)
print("Stopword filtered sentence:"+(" ".join(filtered_text)))