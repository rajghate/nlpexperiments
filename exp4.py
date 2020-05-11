from nltk import pos_tag
from nltk.tokenize import TreebankWordTokenizer,WhitespaceTokenizer,word_tokenize
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.corpus import stopwords
import string
import pandas as pd
from nltk.corpus import wordnet as w

punctuations=[p for p in string.punctuation]
wl=WordNetLemmatizer()
ps=PorterStemmer()
tag_file="tags.txt"
filename="text_english.txt"
stopwords=stopwords.words('english')


with open(tag_file,"r") as file:
    data=file.readlines()
tags_dict={}
for i in data:
    tags_dict[i.split("\t")[0]]=i.split("\t")[1].replace("\n","")
    
with open(filename,"r") as file:
    text=file.read()

text=text.replace("'m"," am")            
text=text.replace("can't","can not")
text=text.replace("won't","will not")



words=[w for w in TreebankWordTokenizer().tokenize(text) if w not in stopwords and w not in punctuations]

#JJ,JJR,JJS=ADJ
#VB VBD VBG VBN VBP=VERB
#RB RBR RBS=ADV
#NN NNS NNP NNPS=NOUN
verb=["VB","VBD" ,"VBG" ,"VBN", "VBP","MD"]
adv=["RB", "RBR", "RBS"]
adj=["JJ","JJR","JJS"]

tags=pos_tag(words)
frame=[]
for word,tag in tags:
    if tag in verb:
        root=wl.lemmatize(word,pos=w.VERB)
    elif tag in adv:
        root=wl.lemmatize(word,pos=w.ADV)
    elif tag in adj:
        root=wl.lemmatize(word,pos=w.ADJ)
    else:
        root=wl.lemmatize(word)
        
    frame.append([word,tags_dict[tag],root])

df=pd.DataFrame(frame,columns=['Word','Tag','Root Word'])

print(df)