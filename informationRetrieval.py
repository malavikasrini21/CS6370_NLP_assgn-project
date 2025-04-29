from util import *
import math
# Add your import statements here




class InformationRetrieval():

	def __init__(self):
		self.index = None

	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""

		index = None

		#Fill in code here
		index = defaultdict(list)  # term -> list of (docID, freq)
		for doc, docID in zip(docs, docIDs):
			term_freq = defaultdict(int)
			for sentence in doc:
				for word in sentence:
					term_freq[word.lower()] += 1  # case-insensitive
			for term, freq in term_freq.items():
				index[term].append((docID, freq))
		self.index = dict(index)


	def rank(self, queries):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""

		doc_IDs_ordered = []

		#Fill in code here
		# Total number of documents
		N = len(set(docID for postings in self.index.values() for docID, _ in postings))

    	# Compute IDF for each term
		idf = {}
		for term, postings in self.index.items():
			df = len(postings)
			idf[term] = math.log(N / df) if df else 0

    	# Build document TF-IDF vectors
		doc_tfidf = {}
		for term, postings in self.index.items():
			for docID, tf in postings:
				if docID not in doc_tfidf:
					doc_tfidf[docID] = {}
				doc_tfidf[docID][term] = tf * idf[term]

    	# Rank documents for each query
		for query in queries:
        	# Compute TF for the query
			query_tf = defaultdict(int)
			for sentence in query:
				for word in sentence:
					query_tf[word.lower()] += 1

        	# Compute TF-IDF for the query
			query_tfidf = {}
			for term, tf in query_tf.items():
				query_tfidf[term] = tf * idf.get(term, 0)

        	# Compute cosine similarity between query and each document
			similarities = []
			for docID, doc_vec in doc_tfidf.items():
				dot_product = sum(query_tfidf.get(term, 0) * doc_vec.get(term, 0)
                              for term in set(query_tfidf.keys()).union(doc_vec.keys()))
				norm_query = math.sqrt(sum(val**2 for val in query_tfidf.values()))
				norm_doc = math.sqrt(sum(val**2 for val in doc_vec.values()))
				if norm_query == 0 or norm_doc == 0:
					similarity = 0
				else:
					similarity = dot_product / (norm_query * norm_doc)
				similarities.append((docID, similarity))

        	# Sort documents by similarity in descending order
			ranked_docs = [docID for docID, _ in sorted(similarities, key=lambda x: x[1], reverse=True)]
			doc_IDs_ordered.append(ranked_docs)
	
		return doc_IDs_ordered




