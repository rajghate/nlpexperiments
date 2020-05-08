
from nltk.stem import PorterStemmer,LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TreebankWordTokenizer

t=TreebankWordTokenizer()
textfile="text_english.txt"
with open(textfile,"r") as file:
    text=file.read()

words=t.tokenize(text)

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