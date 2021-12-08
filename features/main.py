from os import getcwd, listdir, sep, pardir
from os.path import join, normpath
from exploration import avg_length, avg_length_without_filler, filler_count, preprocess, read_file

def main():
	# read all files in data directory
	# store them in a numpy array "corpus"
	# process command line arguments
	# call each feature function
	# collate into one big result matrix
	# interestingCorrelations()
	# trainModel()
	speaker_list = read_file()
	print(speaker_list)

	#functions that need to be preprocessed
	for speaker in speaker_list:
		speaker = preprocess(speaker)
		print('average number of filler words: ', filler_count(speaker))
		print('average length: ', avg_length(speaker))
		print('avg wo filler words: ', avg_length_without_filler(speaker))


if __name__ == "__main__":
	main()