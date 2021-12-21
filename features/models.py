import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score
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

def my_metric(predicted, actual, indices):
	labeled = 0
	unlabeled = 0
	correct_l = 0 #number of correct labeled predictions
	correct_u = 0 #number of correct unlabeled predictions
	for p, a, i, in zip(predicted, actual, indices):
		if a == -1:
			unlabeled += 1
			if p == a:
				correct_u += 1
		else:
			labeled += 1
			if p == a:
				correct_l += 1
	print("Labeled: {:.2%}".format(correct_l / labeled))

def main():
	X = load_features()
	y = load_labels(len(X))
	y_true = y.copy()
	#X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.4, random_state=0)
	base_clf = SVC(probability=True, kernel='linear', C=7, random_state=10)
	#this will fill in the missing labels
	clf = SelfTrainingClassifier(base_clf, threshold=0.7)
	#perform 3 experiments
	#skfolds ensures there are same ratios of labels in test and train sets
	skfolds = StratifiedKFold(n_splits=3)
	for fold, (train_index, test_index) in enumerate(skfolds.split(X, y)):
		X_train = X[train_index]
		y_train = y[train_index]
		X_test = X[test_index]
		y_test = y[test_index]
		y_test_true = y_true[test_index]
		clf.fit(X_train, y_train)
		y_pred = clf.predict(X_test)
		# for i, prediction in enumerate(y_pred):
		# 	print("{:03} predict {} really {}".format(test_index[i], prediction, y_test_true[i]))
		# print("Fold ", fold, " Accuracy: ", accuracy_score(y_test_true, y_pred))
		my_metric(y_pred, y_test_true, test_index)


if __name__ == "__main__":
	main()