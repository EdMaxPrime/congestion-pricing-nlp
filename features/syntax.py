#words like "for" and "the"
from nltk.corpus import stopwords
#used for counting
from nltk.probability import FreqDist
#used to tokenize words
from nltk.tokenize import RegexpTokenizer
#used to stem words 
from nltk.stem.snowball import SnowballStemmer
#used for counting
from collections import Counter
import nltk
import numpy as np
import re

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
	unigrams = np.ndarray(shape=(num_texts, 50), dtype=float, order='C')
	# First, collect all words
	words = [] #contains all words
	breakpoints = [0] #indices into words array between texts
	for text in texts:
		tokens = nltk.word_tokenize(preprocess(text))
		tokens = [word.lower() for word in tokens]
		words += tokens
		breakpoints.append(len(words))
	# Second, determine most common words
	word_counts = FreqDist(words)
	word_counts_ordered = word_counts.most_common()
	headers = [] #the most common 30 words
	for word, count in word_counts_ordered:
		if len(headers) == 50:
			break
		if word not in punct and word not in stopwords.words('english') and word != 'um' and word != 'uh':
			headers.append(word)
	# Next, count how often each of the "most common" appears per text
	for i in range(num_texts):
		#count how often each of the most common words appears
		counts = FreqDist(words[ breakpoints[i]:breakpoints[i+1] ])
		#insert into table
		for j in range(len(headers)):
			unigrams[i][j] = counts[ headers[j] ] / (breakpoints[i+1] - breakpoints[i])
	return unigrams, headers

#remove punctuation and stem for one speaker
def preprocess(speaker):
    #remove punctuation
    speaker = re.sub(r'[^\w\s]', '', speaker)
    #split text
    speaker = speaker.split()
	#stemming words 
    snowstemmer = SnowballStemmer('english')
    for i in range(len(speaker)):
        speaker[i] = snowstemmer.stem(speaker[i])
    #remove stopwords
    # stop_words = set(stopwords.words("english"))
    # speaker = [word for word in speaker if word not in stop_words]
    return ' '.join(speaker)

#Average word length for one text
def avg_length(speaker):
    # print(speaker)
    avg = sum(len(word) for word in speaker) / len(speaker)
    return avg

#Average 
def avg_length_without_filler(speaker):
    without_uh = list(filter(lambda a: a != 'uh' and a != 'um', speaker))
    avg_without_filler = avg_length(without_uh)
    return avg_without_filler


def filler_count(speaker):
    # instances = speaker.count('\s*u[h|m]\s*')
    instances = 0
    # speaker = speaker.split()
    for word in speaker: 
        # print(word)
        if word == 'uh' or word == 'um':
            instances += 1
    return instances

def average_word_length(speakers):
	num_speakers = len(speakers)
	counts = np.ndarray(shape=(num_texts, 3), dtype=float, order='C')
	for i in range(num_speakers):
		tokens = nltk.word_tokenize(speakers[i])
		counts[i][0] = avg_length(tokens)
		counts[i][1] = avg_length_without_filler(tokens)
		counts[i][2] = filler_count(tokens) / len(tokens)
	return counts, ["Avg Length", "Avg Length No Um", "Filler Word Rate"]


# print(preprocess("why should the motorists have to be penalized for something that the city admits it's its own fault"))
