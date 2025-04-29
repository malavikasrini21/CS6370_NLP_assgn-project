# Add your import statements here
import re
import nltk
import string
from collections import defaultdict
import numpy as np
from math import log2

# Add any utility functions here

#Removing Punctuation and extra spaces
def cleaned_text(text):
    text = re.sub(' +',' ',text)
    return text 

def qrel_dic(qrels):
    dictionary = defaultdict(list)
    #Extracting relevant docs
    for qrel in qrels:
        if int(qrel["position"]) <=4:
            dictionary[int(qrel["query_num"])].append(int(qrel['id']))
    return dictionary