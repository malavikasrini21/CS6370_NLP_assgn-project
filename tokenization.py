from util import *

# Add your import statements here




class Tokenization():

    def naive(self, text):
        """
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

        tokenizedText = None

		#Fill in code here  
                  
        tokenizedText = []
        tokenizedText = [[token for token in re.split("[, :;'-]", sentence) if len(token)>0] for sentence in text ]                        
        return tokenizedText



    def pennTreeBank(self, text):
        """
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

        tokenizedText = None

		#Fill in code here
        tokenizer = nltk.tokenize.treebank.TreebankWordTokenizer()
        tokenizedText = [tokenizer.tokenize(sentence) for sentence in text ]

        return tokenizedText