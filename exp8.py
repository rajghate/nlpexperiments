from nltk import TreebankWordTokenizer
import nltk

#sentence=nltk.corpus.treebank.tagged_sents()[22]
sentence=nltk.pos_tag(TreebankWordTokenizer().tokenize("Jim bought 300 shares of Acme Corp in 2006"))
print("Given Sentence:{}".format(sentence))

print(nltk.ne_chunk(sentence,binary=True))
print(nltk.ne_chunk(sentence,binary=True).draw())
