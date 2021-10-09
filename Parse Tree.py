# Creating a Parse Tree through Grammar
import nltk
groucho_grammar = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
""")
sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
parser = nltk.ChartParser(groucho_grammar)
for tree in parser.parse(sent):
    tree.draw()

#importing the treebank corpus
from nltk.corpus import treebank

#parsing a file
tree1 = treebank.parsed_sents('wsj_0001.mrg')[0]
#drawing the parse tree
tree1.draw()

#parsing another file
tree2 = treebank.parsed_sents('wsj_0002.mrg')[0]
#drawing the parse tree
tree2.draw()
