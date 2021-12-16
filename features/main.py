from os import listdir, getcwd
import syntax
import numpy as np


DATA_PATH = "data"
regions = ["Downtown"]


def main():
	# read all files in data directory
	speakers, data, headers = read_files()
	# process command line arguments
	# call each feature function
	data, headers = extract_features(speakers, data, headers)
	# collate into one big result matrix
	# interestingCorrelations()
	text = ",".join(headers) + "\n" + "\n".join(["{},{}".format(row[0], row[1]) for row in data])
	try:
		f = open("features.csv", 'w')
		f.write(text)
		f.close()
	except:
		print("Couldn't save features")
	# trainModel()

# speakers: list of strings, where each string is one speaker
# features_old: same length as speakers, 2d array, one row of data per speaker
# headers: column description
#
# Each function called in here has to do 2 things:
#   parameter: speakers
#   return: features (2d array), headers (list of column descriptions)
#   where features has as many rows as speakers, and as many columns as things
#   it calculates
def extract_features(speakers, features_old, headers):
	features = [features_old]

	f,h = syntax.pronouns(speakers)
	features.append(f)
	headers.extend(h)

	f,h = syntax.most_common(speakers)
	print(h)
	features.append(f)
	headers.extend(h)

	f,h = syntax.average_word_length(speakers)
	features.append(f)
	headers.extend(h)

	all_features = np.concatenate(features,axis=1)
	return all_features, headers


# Returns
# (1) array of strings, the speakers
# (2) matrix for numerical data
# (3) column headers for the matrix
def read_files():
	#list directory
	file_names = listdir(DATA_PATH)
	speakers = []
	data = []
	headers = ["Region", "Order"]
	order = 0             #order of speaking in a meeting
	last_region = ""
	#for each file, read it and append to list
	for filename in file_names:
		region = filename[4:-4]     #get geographic location
		if last_region != region:   #reset counter
			order = 0
			last_region = region
		#read file
		with open("%s/%s" % (DATA_PATH, filename), 'r') as file:
			speakers.append(file.read())
			data.append([regions.index(region), order])
		order += 1
	return speakers, data, headers


if __name__ == "__main__":
	main()