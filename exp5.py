from nltk.util import ngrams
import pandas as pd
from nltk.tokenize import word_tokenize


with open("ngram_corpus.txt","r") as file:
    text=file.read()


tokens=word_tokenize(text)
bigram=list(ngrams(tokens,2))
unigram=list(ngrams(tokens,1))
dict_unigram={}
for i in unigram:
    if i not in dict_unigram.keys():
        dict_unigram[i]=1
    else:
        dict_unigram[i]+=1

dict_bigram={}
for i in bigram:
    if i not in dict_bigram.keys():
        dict_bigram[i]=1
    else:
        dict_bigram[i]+=1

dataunigram=[]
for i in dict_unigram.keys():
    dataunigram.append([i,dict_unigram[i]])

databigram=[]
for i in dict_bigram.keys():
    databigram.append([i,dict_bigram[i]])
    
print(pd.DataFrame(dataunigram,columns=['Unigram','Frequency']))
print(pd.DataFrame(databigram,columns=['Bigram','Frequency']))    

sample_text="I am really sorry for your watch"

bi_gram_test=list(ngrams(word_tokenize("> "+sample_text+" <"),2))
pvalue=1
for i in bi_gram_test:
    pvalue *=dict_bigram[i]/text.count(bi_gram_test[0][1])
    
print("probability of the sentence :\"{}\" \naccording to the given corpus is :{}".format(sample_text,pvalue))