# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:50:10 2020

@author: rajmugdha
"""


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text="This is a sample sentence, showing off the stop words filtration"
stopwords=list(stopwords.words('english'))
words=word_tokenize(text)
filtered_text=[w for w in words if not w in stopwords]
print("original sentence:"+text)
print("Stopword filtered sentence:"+(" ".join(filtered_text)))