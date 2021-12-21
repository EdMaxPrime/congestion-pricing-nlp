#words like "for" and "the"
from nltk.corpus import stopwords
#used for counting
from nltk.probability import FreqDist
#used to tokenize words
from nltk.tokenize import RegexpTokenizer
#used to stem words 
from nltk.stem.snowball import SnowballStemmer
import nltk
#load relevant nltk libraries
nltk.data.path.append("nltk_data")
#used for counting
from collections import Counter
import numpy as np
import re


def pronouns(texts):
	common_pos_tags = ['NN', 'NNP', 'DT', 'IN', 'JJ', 'NNS','CC','PRP','VB','VBG']
	header = ['Noun', 'Proper Noun', 'Determiner', 'Preposition', 'Adjective', 'Noun Plural', 'Coordinating Conjunction', 'Personal Pronoun', 'Verb', 'Verb Grund']
	num_texts = len(texts)
	num_cols = len(header)
	final_counts = np.ndarray(shape=(num_texts, num_cols), dtype=float, order='C')
	for i in range(num_texts):
		tokens = nltk.word_tokenize(texts[i])
		total_tokens = len(tokens)
		tags = nltk.pos_tag(tokens)
		tag_counts = Counter (tag for word, tag in tags)
		for tag in tag_counts:
			tag_counts[tag] /= total_tokens
		for j in range(num_cols):
			# if i == 0:
			# 	print("%s: %d" % (common_pos_tags[j], tag_counts[ common_pos_tags[j] ]))
			final_counts[i][j] = tag_counts[ common_pos_tags[j] ]
	return final_counts, header


#Counts frequencies of most common 50 words in each text
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

# Assumes each text is already tokenized
def search_keywords(texts):
	header = ["climate", "air", "parking", "tax", "disabilities", "transit"]
	num_texts = len(texts)
	num_cols = len(header)
	present = np.zeros((num_texts, num_cols))
	for i, text in enumerate(texts):
		for j, kw in enumerate(header):
			if kw in text:
				present[i][j] = 1
	return present

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
	counts = np.ndarray(shape=(num_speakers, 3), dtype=float, order='C')
	for i in range(num_speakers):
		tokens = nltk.word_tokenize(speakers[i])
		counts[i][0] = avg_length(tokens)
		counts[i][1] = avg_length_without_filler(tokens)
		counts[i][2] = filler_count(tokens) / len(tokens)
	return counts, ["Avg Length", "Avg Length No Um", "Filler Word Rate"]

def my_car(speakers):
	car_array = []
	for speaker in speakers:
		car_array.append([speaker.find("my car") != -1])
	return car_array, ["reference to 'my car'"]

# print(preprocess("why should the motorists have to be penalized for something that the city admits it's its own fault"))
