#from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import codecs

textfile="text_regional.txt"
with codecs.open(textfile,encoding="utf-8") as file:
    text=file.read()
with codecs.open("final_stopwords.txt",encoding="utf-8") as file:
    stopwordstext=file.read()


#stopwords=list(stopwords.words('hindi'))
stopwords=stopwordstext.split("\n")
words=word_tokenize(text)
filtered_text=[w for w in words if not w in stopwords]
print("original text\n:"+text)
print("Stopword filtered text\n:"+(" ".join(filtered_text)))