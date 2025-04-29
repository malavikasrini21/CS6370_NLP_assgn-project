import nltk
from collections import Counter
from nltk.tokenize import word_tokenize
import string

# Download necessary resources
# nltk.download('punkt')
# nltk.download('stopwords')

from nltk.corpus import stopwords

# Sample Cranfield Dataset (Subset)
documents = [
    "The analysis of airflow over an aircraft is crucial in aerodynamics.",
    "Aircraft performance depends on airflow and pressure distribution.",
    "The study of aerodynamics helps in improving aircraft efficiency.",
    "Pressure variation affects the performance of an aircraft significantly.",
    "Aircraft design and airflow dynamics influence stability."
]

# Tokenize and clean text
word_list = []
doc_word_lists = []  # Store tokenized words per document

for doc in documents:
    words = word_tokenize(doc.lower())  # Convert to lowercase
    words = [word for word in words if word not in string.punctuation]  # Remove punctuation
    word_list.extend(words)
    doc_word_lists.append(set(words))  # Store unique words per document

# Count word frequency
word_freq = Counter(word_list)

# Set threshold: Words appearing in at least 75% of documents
threshold = len(documents) * 0.75  
corpus_stopwords = {word for word, freq in word_freq.items() if sum(1 for doc in doc_word_lists if word in doc) >= threshold}

# Get NLTK stopwords
nltk_stopwords = set(stopwords.words('english'))

# Compare stopwords
print("Corpus-Specific Stopwords:", corpus_stopwords)
print("\nNLTK Stopwords:", nltk_stopwords)

# Words found in both sets
common_stopwords = corpus_stopwords.intersection(nltk_stopwords)
print("\nCommon Stopwords:", common_stopwords)

# Words unique to corpus-based approach
unique_corpus_stopwords = corpus_stopwords - nltk_stopwords
print("\nCorpus-Specific Stopwords (Not in NLTK List):", unique_corpus_stopwords)

# Words unique to NLTK stopwords
unique_nltk_stopwords = nltk_stopwords - corpus_stopwords
print("\nNLTK Stopwords (Not in Corpus-Based List):", unique_nltk_stopwords)
