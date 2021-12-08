# from features.exploration import read_file 
from exploration import read_file

def main():
	# read all files in data directory
	# store them in a numpy array "corpus"
	# process command line arguments
	# call each feature function
	# collate into one big result matrix
	# interestingCorrelations()
	# trainModel()
	speaker = read_file()
	print(speaker)

if __name__ == "__main__":
	main()