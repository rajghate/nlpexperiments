from nltk.tag import tnt
from nltk.corpus import indian
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
import codecs
from googletrans import Translator
import re
import pandas as pd


translator=Translator()
train_data=indian.tagged_sents('hindi.pos')
t=tnt.TnT()
t.train(train_data)
filename="hmmdata_hindi.txt"

with codecs.open(filename,encoding="utf-8") as file:
    text=file.read()
text= "eos "+text
text=text.replace("|"," eos")

words=[w for w in word_tokenize(text) if w not in [".",","] and w !="eos"]
tags=t.tag(words)
j=0
for i in word_tokenize(text):
    if i =="eos":
        tags.insert(j,('eos','EOS'))
    j+=1
word_pos=[]
with open("updated_tags.txt","r") as file:
    data=file.readlines()
tags_dict={}
for i in data:
    tags_dict[i.split("\t")[0]]=i.split("\t")[1].replace("\n","")
for i,j in tags:
  if j=="Unk":
    tr=translator.translate(i)
    tag=pos_tag([tr.text])[0][1]
  else:
    tag=j
  word_pos.append((i,tags_dict[tag]))
tag_list=[w[1] for w in word_pos]
word_pos_dict = {}
for i in word_pos:
    if i not in list(word_pos_dict.keys()):
        word_pos_dict[i]=1
    else:
        word_pos_dict[i]+=1
tag_bigram_dict={}
for i in list(ngrams(tag_list,2)):
    if i not in tag_bigram_dict.keys():
        tag_bigram_dict[i]=1
    else:
        tag_bigram_dict[i]+=1
tag_dict={}
for i in tag_list:
    if i not in tag_dict.keys():
        tag_dict[i]=1
    else:
        tag_dict[i]+=1
emmision_matrix=[]
transition_matrix=[]
for i in sorted(set(tag_list)):
    temp=[]
    for j in sorted(set(word_tokenize(text.lower()))):
        temp.append(word_pos.count((j,i))/tag_dict[i])
    emmision_matrix.append(temp)
for i in sorted(set(tag_list)):
    temp=[]
    for j in sorted(set(tag_list)):
        temp.append(list(ngrams(tag_list,2)).count((j,i))/tag_list.count(i))
    transition_matrix.append(temp)

import pandas as pd

em=pd.DataFrame(emmision_matrix)
em.columns=sorted(set(word_tokenize(text.lower())))
em.index=sorted(set(tag_list))

tm=pd.DataFrame(transition_matrix)
tm.columns=sorted(set(tag_list)).copy()
tm.index=sorted(set(tag_list)).copy()

print("POS Tags:\n{}".format(word_pos))
print("Word->Tag count:\n{}".format(word_pos_dict))
print("Emmision Matrix:\n{}".format(em))
print("Transition Matrix:\n{}".format(tm))

