#importing nltk
import nltk 

#importing the inaugural corpus
from nltk.corpus import inaugural

#counting the occurrences 
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids() 
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target)) #convert the corpus to lowercase and examine

#plotting the curve 
cfd.plot()