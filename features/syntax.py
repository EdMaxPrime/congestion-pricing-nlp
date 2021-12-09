import nltk
nltk.data.path.append("venv/nltk_data")
nltk.download("punkt", download_dir="venv/nltk_data")
nltk.download("averaged_perceptron_tagger", download_dir="venv/nltk_data")

def pronouns(speakers, data, headers):
	for i in range(len(speakers)):
		data[i].append(0)
	headers.append("Test")