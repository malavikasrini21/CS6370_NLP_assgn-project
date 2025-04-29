from util import *

# Add your import statements here




class SentenceSegmentation():

    def naive(self, text):
        """
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""
        

		#Fill in code here
        #Splitting with [?!.\n] and removing spaces
        segmentedText = [ele for ele in re.split("[?!.\n]",text) if ele.strip()]
        return segmentedText


    def punkt(self, text):
        """
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""

        segmentedText = None
        

		#Fill in code here
        tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
        segmentedText = tokenizer.tokenize(text)
		
        return segmentedText