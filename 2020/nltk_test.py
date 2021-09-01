import nltk 
import re

wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]

# print(wordlist)
ed_words = [w for w in wordlist if re.search('ed$', w)]

print(ed_words)


import unicodedata