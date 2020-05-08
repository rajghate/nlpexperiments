'''
A Lightweight Stemmer for Hindi
    Ananthakrishnan Ramanathan and Durgesh D Rao
    http://computing.open.ac.uk/Sites/EACLSouthAsia/Papers/p6-Ramanathan.pdf

    @conference{ramanathan2003lightweight,
      title={{A lightweight stemmer for Hindi}},
      author={Ramanathan, A. and Rao, D.},
      booktitle={Workshop on Computational Linguistics for South-Asian Languages, EACL},
      year={2003}
    }

'''
suffixes = {
    1: ["ो", "े", "ू", "ु", "ी", "ि", "ा"],
    2: ["कर", "ाओ", "िए", "ाई", "ाए", "ने", "नी", "ना", "ते", "ीं", "ती", "ता", "ाँ", "ां", "ों", "ें"],
    3: ["ाकर", "ाइए", "ाईं", "ाया", "ेगी", "ेगा", "ोगी", "ोगे", "ाने", "ाना", "ाते", "ाती", "ाता", "तीं", "ाओं", "ाएं", "ुओं", "ुएं", "ुआं"],
    4: ["ाएगी", "ाएगा", "ाओगी", "ाओगे", "एंगी", "ेंगी", "एंगे", "ेंगे", "ूंगी", "ूंगा", "ातीं", "नाओं", "नाएं", "ताओं", "ताएं", "ियाँ", "ियों", "ियां"],
    5: ["ाएंगी", "ाएंगे", "ाऊंगी", "ाऊंगा", "ाइयाँ", "ाइयों", "ाइयां"],
}

def hi_stem(word):
    for L in 5, 4, 3, 2, 1:
        if len(word) > L + 1:
            for suf in suffixes[L]:
                if word.endswith(suf):
                    return word[:-L]
    return word

import codecs
from nltk.tokenize import TreebankWordTokenizer


t=TreebankWordTokenizer()
textfile="text_regional.txt"

with codecs.open(textfile,encoding="utf-8") as file:
    text=file.read()
words=t.tokenize(text)
print("{0:20}{1:20}".format("Word","stemmed output")) 
for w in words:
    print ("{0:20}{1:20}".format(w,hi_stem(w)))