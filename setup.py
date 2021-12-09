# Run this script before features/main.py
# But after $pip3 install -r requirements.txt
# This will download extra nltk packages

import nltk
nltk.data.path.append("nltk_data")
nltk.download("punkt", download_dir="nltk_data")
nltk.download("averaged_perceptron_tagger", download_dir="nltk_data")
nltk.download("stopwords", download_dir="nltk_data")