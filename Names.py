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