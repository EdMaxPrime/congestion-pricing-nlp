from os import getcwd, listdir, sep, pardir
from os.path import join, normpath
from exploration import avg_length, avg_length_without_filler, filler_count, preprocess

def main():
	# read all files in data directory
	# store them in a numpy array "corpus"
	# process command line arguments
	# call each feature function
	# collate into one big result matrix
	# interestingCorrelations()
	# trainModel()
	go_back = normpath(getcwd() + sep + pardir)
	print(go_back)
	directory_name = join(go_back, 'sourcing/data')
	directory = listdir(directory_name)
	print(directory)
    #for each file in data directory
	for filename in directory:
        #read the content of each
		if filename.endswith('.txt'):
			with open(join(directory_name, filename)) as f:
				speaker = f.read()
				speaker = preprocess(speaker)
				print('average number of filler words: ', filler_count(speaker))
				print('average length: ', avg_length(speaker))
				print('avg wo filler words: ', avg_length_without_filler(speaker))

if __name__ == "__main__":
	main()