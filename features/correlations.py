from models import get_predictions

# Inspect the features of the text and print interesting correlations
def correlations():
	data, headers, labels = get_predictions()
	print(labels)

if __name__ == "__main__":
	correlations()