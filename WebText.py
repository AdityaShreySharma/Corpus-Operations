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