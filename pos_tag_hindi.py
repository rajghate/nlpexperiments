from nltk.tag import 
from nltk.corpus import indian
import codecs

train_data=indian.tagged_sents('hindi.pos')
t=tnt.TnT()
t.train(train_data)
filename="text_regional.txt"

with codecs.open(filename,mode="r",encoding="utf-8") as file:
    data=file.read()
    
    
