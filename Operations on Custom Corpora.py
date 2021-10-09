#importing nltk
import nltk
#installing all the custom corpora
nltk.download()


# importing libraries
import os, os.path
# using the given path
path = os.path.expanduser("~/nltk_data")
# checking
if not os.path.exists(path):
    os.mkdir(path)
print("\n")
print ("Path Exists = ", os.path.exists(path))
import nltk.data
print ("Path Exists in NLTK = ", path in nltk.data.path)



#-----------------------------------------------------------------------------------------------------------------------
#********************************************WORD FREQUENCY IDENTIFICATION**********************************************
#-----------------------------------------------------------------------------------------------------------------------


# a) Using the UDHR (Universal Declaration of Human Rights) Corpus 
# To examine the differences in word lengths for a selection of languages included in this corpus
#importing nltk
import nltk 
#importing the corpus udhr
from nltk.corpus import udhr
#selected languages for testing
languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
#examining the difference in word lengths
cfd = nltk.ConditionalFreqDist(
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latin1'))
#plotting the Samples vs Counts curve
cfd.plot(cumulative=True)


# b) Using the WebText Corpus to count the number of words in this corpus having a frequency of greater than 3
#importing nltk 
import nltk
#importing the webtext corpus
from nltk.corpus import webtext
# downloading the webtext package 
nltk.download('webtext')
wt_words = webtext.words('firefox.txt')
data_analysis = nltk.FreqDist(wt_words)
#taking the specific words only if their frequency is greater than 3.
filter_words = dict([(m, n) for m, n in data_analysis.items() if len(m) > 3])
data_analysis = nltk.FreqDist(filter_words)
#plotting the Words vs Counts curve
data_analysis.plot(25, cumulative=False)


# c) Using the Names Corpus, which contains 8000 first names categorized by gender, 
# To find names which appear in both files, i.e. names that are ambiguous for gender. 
# The male and female names are stored in separate files
#importing nltk 
import nltk
#importing the names corpus and storing it in a variable 
names = nltk.corpus.names
#comparing the gender-wise ambiguous names
cfd = nltk.ConditionalFreqDist(
    (fileid, name[-1])
    for fileid in names.fileids()
    for name in names.words(fileid))
#plotting the Samples vs Counts curve
cfd.plot()



#-----------------------------------------------------------------------------------------------------------------------
#***************************************CORPUS ANNOTATION (POS TAGGING)*************************************************
#-----------------------------------------------------------------------------------------------------------------------


# a) Using a section of the Gutenberg Corpus to add POS tags for each individual word
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


# b) Using the Brown Corpus to find out the words that are highly ambiguous as to their part of speech tag
#importing the required dependencies and corpus
import nltk
from nltk.corpus import brown
#tagging the words from the news category
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
#testing for ambiguity among the POS tags
data = nltk.ConditionalFreqDist((word.lower(), tag)
for (word, tag) in brown_news_tagged)
for word in sorted(data.conditions()):
    if len(data[word]) > 3:
        tags = [tag for (tag, _) in data[word].most_common()]
        print(word, ' '.join(tags))



#-----------------------------------------------------------------------------------------------------------------------
#************************************Creating Parse Trees using the Treebank Corpus*************************************
#-----------------------------------------------------------------------------------------------------------------------


#Creating Parse Trees using the Treebank Corpus
#importing the treebank corpus
import nltk
from nltk.corpus import treebank
#parsing a file
tree1 = treebank.parsed_sents('wsj_0001.mrg')[0]
#drawing the parse tree
tree1.draw()
#parsing another file
tree2 = treebank.parsed_sents('wsj_0002.mrg')[0]
#drawing the parse tree
tree2.draw()