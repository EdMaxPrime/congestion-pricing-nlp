from models import get_predictions
import matplotlib.pyplot as plt

# Inspect the features of the text and print interesting correlations
def correlations():
	data, headers, labels = get_predictions()
	print(labels)
	y_pronouns = data[:, headers.index("sentiment")]
	plt.scatter(labels, y_pronouns)
	plt.xlabel("Stance")
	plt.ylabel("Compound Sentiment Scores")
	plt.show()


if __name__ == "__main__":
	correlations()