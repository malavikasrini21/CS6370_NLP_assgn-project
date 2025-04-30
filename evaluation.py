from util import *
import math

# Add your import statements here




class Evaluation():

	def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

		precision = -1

		#Fill in code here
		top_k_docs = query_doc_IDs_ordered[:k]
		# Count how many of the top k documents are in the true_doc_IDs (relevant documents)
		relevant_count = sum(1 for doc_id in top_k_docs if doc_id in true_doc_IDs)
		# Precision is the number of relevant documents in the top k divided by k
		precision = relevant_count / k

		return precision


	def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""

		meanPrecision = -1

		#Fill in code here
		total_precision = 0.0
		num_queries = len(query_ids)
		for i in range(num_queries):
			query_id = query_ids[i]
			predicted_docs = doc_IDs_ordered[i]
			# Extract relevant documents for this query from qrels
			true_doc_IDs = [int(rel['id']) for rel in qrels if int(rel['query_num']) == query_id]
			# Compute precision for this query
			precision = self.queryPrecision(predicted_docs, query_id, true_doc_IDs, k)
			total_precision += precision
			
		meanPrecision = total_precision / num_queries if num_queries > 0 else 0.0

		return meanPrecision

	
	def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		recall = -1

		#Fill in code here
		top_k_docs = query_doc_IDs_ordered[:k]
		# Count how many of the top k documents are in the true relevant documents
		relevant_retrieved = sum(1 for doc_id in top_k_docs if doc_id in true_doc_IDs)
		# Avoid division by zero
		if len(true_doc_IDs) == 0:
			recall = 0.0
		else:
			# Recall is the number of relevant documents retrieved divided by total relevant documents
			recall = relevant_retrieved / len(true_doc_IDs)

		return recall


	def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""

		meanRecall = -1

		#Fill in code here
		total_recall = 0.0
		num_queries = len(query_ids)
		for i in range(num_queries):
			query_id = query_ids[i]
			predicted_docs = doc_IDs_ordered[i]
			# Extract relevant documents for this query from qrels
			true_doc_IDs = [int(rel['id']) for rel in qrels if int(rel['query_num']) == query_id]
			# Compute recall for this query
			recall = self.queryRecall(predicted_docs, query_id, true_doc_IDs, k)
			total_recall += recall
		meanRecall = total_recall / num_queries if num_queries > 0 else 0.0


		return meanRecall


	def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

		fscore = -1

		#Fill in code here
		# Calculate precision and recall for the query
		precision = self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		recall = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		# Avoid division by zero
		if precision + recall == 0:
			fscore = 0.0
		else:
			# Harmonic mean of precision and recall
			fscore = 2 * (precision * recall) / (precision + recall)

		return fscore


	def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""

		meanFscore = -1

		#Fill in code here
		total_fscore = 0.0
		num_queries = len(query_ids)
		for i in range(num_queries):
			query_id = query_ids[i]
			predicted_docs = doc_IDs_ordered[i]
			# Extract relevant documents for this query from qrels
			true_doc_IDs = [int(rel['id']) for rel in qrels if int(rel['query_num']) == query_id]
			# Compute fscore for this query
			fscore = self.queryFscore(predicted_docs, query_id, true_doc_IDs, k)
			total_fscore += fscore
		meanFscore = total_fscore / num_queries if num_queries > 0 else 0.0

		return meanFscore
	

	def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""

		nDCG = -1

		#Fill in code here
		# Compute DCG
		DCG = 0.0
		for i in range(min(k, len(query_doc_IDs_ordered))):
			doc_id = query_doc_IDs_ordered[i]
			if doc_id in true_doc_IDs:
				DCG += 1 / math.log2(i + 2)  # i+2 because log2(1) = 0 for i=0
		# Compute IDCG (ideal DCG)
		ideal_hits = min(k, len(true_doc_IDs))
		IDCG = sum(1 / math.log2(i + 2) for i in range(ideal_hits))
		# Compute nDCG
		nDCG = DCG / IDCG if IDCG > 0 else 0.0

		return nDCG


	def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""

		meanNDCG = -1

		#Fill in code here
		total_nDCG = 0.0
		num_queries = len(query_ids)
		for i in range(num_queries):
			query_id = query_ids[i]
			predicted_docs = doc_IDs_ordered[i]
			# Extract relevant documents for this query from qrels
			true_doc_IDs = [int(rel['id']) for rel in qrels if int(rel['query_num']) == query_id]
			# Compute nDCG for this query
			nDCG = self.queryNDCG(predicted_docs, query_id, true_doc_IDs, k)
			total_nDCG += nDCG
		meanNDCG = total_nDCG / num_queries if num_queries > 0 else 0.0

		return meanNDCG


	def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""

		avgPrecision = -1

		#Fill in code here
		relevant_found = 0
		precision_sum = 0.0
		for i in range(min(k, len(query_doc_IDs_ordered))):
			doc_id = query_doc_IDs_ordered[i]
			if doc_id in true_doc_IDs:
				relevant_found += 1
				precision = relevant_found / (i + 1)
				precision_sum += precision
		avgPrecision = precision_sum / len(true_doc_IDs) if len(true_doc_IDs) > 0 else 0.0

		return avgPrecision


	def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""

		meanAveragePrecision = -1

		#Fill in code here
		total_ap = 0.0
		num_queries = len(query_ids)
		for i in range(num_queries):
			query_id = query_ids[i]
			predicted_docs = doc_IDs_ordered[i]
			# Get relevant documents for this query
			true_doc_IDs = [int(rel['id']) for rel in q_rels if int(rel['query_num']) == query_id]
			# Compute average precision for this query
			ap = self.queryAveragePrecision(predicted_docs, query_id, true_doc_IDs, k)
			total_ap += ap
		meanAveragePrecision = total_ap / num_queries if num_queries > 0 else 0.0


		return meanAveragePrecision

