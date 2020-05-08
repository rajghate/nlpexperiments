# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:50:10 2020

@author: rajmugdha
"""


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

textfile="text_english.txt"
with open(textfile,"r") as file:
    text=file.read()

stopwords=list(stopwords.words('english'))
words=word_tokenize(text)
filtered_text=[w for w in words if not w in stopwords]
print("original text \n:"+text)
print("Stopword filtered text \n:"+(" ".join(filtered_text)))