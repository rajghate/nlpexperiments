from nltk.tokenize import word_tokenize,sent_tokenize

textfile="text_english.txt"
with open(textfile,"r") as file:
    text=file.read()
words=word_tokenize(text)
sentences=sent_tokenize(text)

print("words:"+str(words))
print("sentences:"+str(sentences))