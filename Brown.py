import nltk
print(nltk.corpus.brown.tagged_words())

from nltk.corpus import brown
print(brown.words())

brown_lrnd_tagged = brown.tagged_words(categories='learned', tagset='universal')
tags = [b[1] for (a, b) in nltk.bigrams(brown_lrnd_tagged) if a[0] == 'often']
fd = nltk.FreqDist(tags)
fd.tabulate()

from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
unigram_tagger.tag(brown_sents[2007])
print("Probability = ", unigram_tagger.evaluate(brown_tagged_sents))

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
