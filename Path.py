# #importing nltk
import nltk

# #installing all the custom corpora
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


