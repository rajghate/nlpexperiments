from nltk.tag import tnt,pos_tag
from nltk.corpus import indian
from nltk.tokenize import TreebankWordTokenizer
import codecs
from googletrans import Translator
import re
import pandas as pd


translator=Translator()
train_data=indian.tagged_sents('hindi.pos')
t=tnt.TnT()
t.train(train_data)
filename="text_regional.txt"

with codecs.open(filename,encoding="utf-8") as file:
    data=file.read()
with codecs.open("final_stopwords.txt",encoding="utf-8") as file:
    stopwordstext=file.read()


#stopwords=list(stopwords.words('hindi'))
stopwords=stopwordstext.split("\n")    

words=[w for w in TreebankWordTokenizer().tokenize(data) if w not in stopwords and w not in ["|",".",","]]
tags=t.tag(words)
tag_list=[]
for i,j in tags:
  if j=="Unk":
    tr=translator.translate(i)
    tag=pos_tag([tr.text])[0][1]
  else:
    tag=j
  tag_list.append([i,tag])

suffixes = {
	    1: ["ो", "े", "ू", "ु", "ी", "ि", "ा"],  
            2: ["तृ","ान","ैत","ने","ाऊ","ाव","कर", "ाओ", "िए", "ाई", "ाए", "नी", "ना", "ते", "ीं", "ती",
                "ता", "ाँ", "ां", "ों", "ें","ीय", "ति","या", "पन", "पा","ित","ीन","लु","यत","वट","लू"],     
            3: ["ेरा","त्व","नीय","ौनी","ौवल","ौती","ौता","ापा","वास","हास","काल","पान","न्त","ौना","सार","पोश","नाक",
                "ियल","ैया", "ौटी","ावा","ाहट","िया","हार", "ाकर", "ाइए", "ाईं", "ाया", "ेगी", "वान", "बीन",
                "ेगा", "ोगी", "ोगे", "ाने", "ाना", "ाते", "ाती", "ाता", "तीं", "ाओं", "ाएं", "ुओं", "ुएं", "ुआं","कला","िमा","कार",
                "गार", "दान","खोर"],     
            4: ["ावास","कलाप","हारा","तव्य","वैया", "वाला", "ाएगी", "ाएगा", "ाओगी", "ाओगे", 
                "एंगी", "ेंगी", "एंगे", "ेंगे", "ूंगी", "ूंगा", "ातीं", "नाओं", "नाएं", "ताओं", "ताएं", "ियाँ", "ियों", "ियां",
                "त्वा","तव्य","कल्प","िष्ठ","जादा","क्कड़"],     
            5: ["ाएंगी", "ाएंगे", "ाऊंगी", "ाऊंगा", "ाइयाँ", "ाइयों", "ाइयां", "अक्कड़","तव्य:","निष्ठ"],
}

special_suffixes = ["र्", "ज्य","त्य"]
dict_special_suffixes = {"र्":"ृ",
                         "ज्य":"ज्",
                         "त्य":"त्"}
words_dict  = { "तैराक":"तैर",
                "चालाक":"चाल",
                "कूलाक":"कूल",
                "बेलन":"बेल",
                "मिलाप":"मिल",
                "चुपचाप": "चुप",
                "निकास":"निकस",
                "लुकास":"लुक",
                }

def hi_stem(word):
    ans = word
    bl = False
    
    if word in words_dict.keys():
        return words_dict[word]
    
    for L in 5, 4, 3, 2, 1:
        if len(word) > L + 1:
            for suf in suffixes[L]:
                if word.endswith(suf):
                    ans = word[:-L]
                    bl =True
        if bl == True:
            break
                    
    if bl == True:
        for suf in suffixes[1]:
            if ans.endswith(suf):
                # use case - गानेवाला
                ans = hi_stem(ans)
   
    for suf in special_suffixes:
        if ans.endswith(suf):
            l = len(suf)
            ans = ans[:-l]
            ans += dict_special_suffixes[suf]
 
    return ans
frame=[]
with open("tags.txt","r") as file:
    data=file.readlines()
tags_dict={}
for i in data:
    tags_dict[i.split("\t")[0]]=i.split("\t")[1].replace("\n","")

for word,tag in tag_list:
  root_word=hi_stem(word)
  frame.append([word,tags_dict[tag],root_word])

df=pd.DataFrame(frame,columns=['word','tag','root word'])
print(df)