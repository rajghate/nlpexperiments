from nltk import RegexpParser
import nltk

def ie_preprocess(document):
    sentences=nltk.sent_tokenize(document)
    sent_tokens=[]
    for sent in sentences:
        tokens=[w for w in nltk.word_tokenize(sent) if w !="."]
        sent_tokens.append(tokens)
    pos_tag_sent=[]
    for token in sent_tokens:
        temp=nltk.pos_tag(token)
        pos_tag_sent.append(temp)
    return pos_tag_sent
    

with open("hmmdata.txt","r") as file:
    data=file.read()
#data=data.replace(".","")
data=data+" the little yellow dog barked at the cat."
sentences=ie_preprocess(data)
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp=RegexpParser(grammar)
for i in range(len(sentences)):
      result=cp.parse(sentences[i])
      print(result.draw())
    
