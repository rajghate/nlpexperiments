from nltk.tokenize import word_tokenize,sent_tokenize
import codecs

textfile="text_regional.txt"
with codecs.open(textfile,encoding="utf-8") as file:
    text=file.read()

words=word_tokenize(text)
sentences=text.split("|")

print("words:"+str(words))
print("sentences:"+str(sentences))