import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from main import load_features
from sys import exit
from pathlib import Path

# NUM_FEATURES = 3
# NUM_SAMPLES = 100

# def mapping(x):
# 	if x[0] < x[1]:
# 		return 0
# 	elif x[0] < x[2]:
# 		return 1
# 	else:
# 		return 2

# features = np.random.rand(NUM_SAMPLES, NUM_FEATURES)
# target = list(map(mapping, features))
# print("Target: ", target)

# X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.4, random_state=0)

# clf = SVC(kernel='linear', C=1).fit(X_train, y_train)
# print("Score: ", clf.score(X_test, y_test))


def load_labels(num_samples):
	try:
		labels = np.full(num_samples, -1, dtype=int) #array full of -1
		p = Path(__file__).with_name('Speakers_labeled.csv')
		csv = [row.split(",") for row in p.open('r')]
		print("Opened labels file")
		for row in csv[1:]:
			try:
				idx = int(row[0])
				val = int(row[2])
				labels[ idx ] = val
			except:
				print("Failed to convert ", row[0])
		return labels
	except:
		exit("Couldn't find labeled data in Speakers_labeled.csv")



def main():
	data = load_features()
	target = load_labels(len(data))
	X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.4, random_state=0)
	clf = SVC(kernel='linear', C=1).fit(X_train, y_train)
	print("Score: ", clf.score(X_test, y_test))

if __name__ == "__main__":
	main()