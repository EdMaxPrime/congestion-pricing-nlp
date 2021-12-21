import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score
from main import load_features, load_labels



def get_predictions():
	X, headers = load_features()
	y = load_labels(len(X))
	predictions = y.copy()
	#this classifier will be used to fill in the missing labels
	base_clf = SVC(probability=True, kernel='linear', C=7, random_state=10)
	#this classifier will be used for final predictions
	clf = SelfTrainingClassifier(base_clf, threshold=0.7)
	#perform 3 experiments
	#skfolds ensures there are same ratios of labels in test and train sets
	skfolds = StratifiedKFold(n_splits=3)
	for fold, (train_index, test_index) in enumerate(skfolds.split(X, y)):
		X_train = X[train_index]
		y_train = y[train_index]
		X_test = X[test_index]
		y_test = y[test_index]
		y_test_true = y[test_index]
		clf.fit(X_train, y_train)
		y_pred = clf.predict(X_test)
		for fold_i, actual_i in enumerate(test_index):
			if predictions[actual_i] == -1:
				predictions[actual_i] = y_pred[fold_i]
	return X, headers, predictions


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
	score = correct_l / labeled
	return score

def main():
	X, _ = load_features()
	y = load_labels(len(X))
	#this classifier will be used to fill in the missing labels
	base_clf = SVC(probability=True, kernel='linear', C=7, random_state=10)
	#this classifier will be used for final predictions
	clf = SelfTrainingClassifier(base_clf, threshold=0.7)
	#perform 3 experiments
	#skfolds ensures there are same ratios of labels in test and train sets
	skfolds = StratifiedKFold(n_splits=3)
	for fold, (train_index, test_index) in enumerate(skfolds.split(X, y)):
		X_train = X[train_index]
		y_train = y[train_index]
		X_test = X[test_index]
		y_test = y[test_index]
		y_test_true = y[test_index]
		clf.fit(X_train, y_train)
		y_pred = clf.predict(X_test)
		# for i, prediction in enumerate(y_pred):
		# 	print("{:03} predict {} really {}".format(test_index[i], prediction, y_test_true[i]))
		# print("Fold ", fold, " Accuracy: ", accuracy_score(y_test_true, y_pred))
		print("Labeled: {:.2%}".format(my_metric(y_pred, y_test_true, test_index)))


if __name__ == "__main__":
	main()