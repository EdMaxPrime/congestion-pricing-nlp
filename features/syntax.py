#words like "for" and "the"
from nltk.corpus import stopwords
#used for counting
from nltk.probability import FreqDist
#used to tokenize words
from nltk.tokenize import RegexpTokenizer
#used for counting
from collections import Counter
import nltk
nltk.data.path.append("nltk_data")
nltk.download("punkt", download_dir="nltk_data")
nltk.download("averaged_perceptron_tagger", download_dir="nltk_data")
nltk.download("stopwords", download_dir="nltk_data")
import numpy as np

def pronouns(speakers):
	f = []
	for i in range(len(speakers)):
		f.append([0])
	h = ["Test"]
	return f, h


def most_common(texts):
	# don't count punctuation
	punct = ['.', ',', ':', ';', '-', "\'", "\"", '(', ")", '!', '?', "...", "``", "\'\'"]
	num_texts = len(texts)
	unigrams = np.ndarray(shape=(num_texts, 30), dtype=float, order='C')
	# First, collect all words
	words = [] #contains all words
	breakpoints = [0] #indices into words array between texts
	for text in texts:
		tokens = nltk.word_tokenize(text)
		tokens = [word.lower() for word in tokens]
		words += tokens
		breakpoints.append(len(words))
	# Second, determine most common words
	word_counts = FreqDist(words)
	word_counts_ordered = word_counts.most_common()
	headers = [] #the most common 30 words
	for word, count in word_counts_ordered:
		if len(headers) == 30:
			break
		if word not in punct and word not in stopwords.words('english'):
			headers.append(word)
	# Next, count how often each of the "most common" appears per text
	for i in range(num_texts):
		#count how often each of the most common words appears
		counts = FreqDist(words[ breakpoints[i]:breakpoints[i+1] ])
		#insert into table
		for j in range(len(headers)):
			unigrams[i][j] = counts[ headers[j] ] / (breakpoints[i+1] - breakpoints[i])
	return unigrams, headers