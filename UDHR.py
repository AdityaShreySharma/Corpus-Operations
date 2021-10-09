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