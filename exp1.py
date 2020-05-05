from nltk.tokenize import word_tokenize,sent_tokenize

text=input("enter text:")
words=word_tokenize(text)
sentences=sent_tokenize(text)

print("words:"+str(words))
print("sentences:"+str(sentences))