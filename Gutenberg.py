import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

sample = gutenberg.raw("bible-kjv.txt")
tok = sent_tokenize(sample)
print(tok[5:15])

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)

#importing the required corpora and dependencies
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.corpus import gutenberg

#using english stop words
stop_words = set(stopwords.words('english'))

#importing the file "bible-kjv.txt" from the gutenberg corpus
txt = gutenberg.raw("bible-kjv.txt")  

#tokenizing the text file from the corpus
tok = sent_tokenize(txt)

#extracting a section out of the file
tokenize = tok[5:15]

#tagging 
for i in tokenize:
    wordsList = nltk.word_tokenize(i)
    wordsList = [w for w in wordsList if not w in stop_words] 
    tagged = nltk.pos_tag(wordsList)
    print(tagged)