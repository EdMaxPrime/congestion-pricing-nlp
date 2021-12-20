import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np

nltk.data.path.append("nltk_data")

def vader(speakers):
	num_speakers = len(speakers)
	headers = ["positive words", "neutral_words", "negative words", "sentiment"]
	feels = np.ndarray(shape=(num_speakers, len(headers)), dtype=float, order='C')
	#Sentiment Analyzer
	sid = SentimentIntensityAnalyzer()
	for i in range(num_speakers):
		x = sid.polarity_scores(speakers[i])
		feels[i][0] = x["pos"]
		feels[i][1] = x["neu"]
		feels[i][2] = x["neg"]
		feels[i][3] = x["compound"]
	return feels, headers