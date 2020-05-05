# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:15:19 2020

@author: rajmugdha
"""


from nltk.stem import PorterStemmer,LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

words=word_tokenize("He was running and eating at same time. He has bad habit of swimming after playing long hours in the Sun.")

wordnet_lemmatizer=WordNetLemmatizer()
porterStemmer=PorterStemmer()
lancasterStemmer=LancasterStemmer()

porter_stem_words=[porterStemmer.stem(word) for word in words]
print("Porter Stemming Output \n"+str(porter_stem_words))

punctuations="?:!.,;"
for word in words:
    if word in punctuations:
        words.remove(word)

print("Lemmatization output:")
print("{0:20}{1:20}".format("Word","Lemma"))        
for word in words:
    print ("{0:20}{1:20}".format(word,wordnet_lemmatizer.lemmatize(word,pos="v")))