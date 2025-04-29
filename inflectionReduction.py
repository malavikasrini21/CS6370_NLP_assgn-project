from util import *

# Add your import statements here




class InflectionReduction:
    def reduce(self, text):
        """
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

        reducedText = None

		#Fill in code here
        porter_stemmer = nltk.stem.PorterStemmer()
        reducedText = [[porter_stemmer.stem(word) for word in sentence] for sentence in text]
		
        return reducedText

