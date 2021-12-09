from os import listdir, getcwd, mkdir
from os.path import join, dirname, exists
import re

DATA_PATH = "data"
SRC_PATH = "sourcing"
SPEAKER = re.compile("===")
NEW_LINE = re.compile("\n\n")

original_files = listdir(SRC_PATH)
next_file = 0
first_file = 0

# create data directory
if not exists(DATA_PATH):
	mkdir(DATA_PATH)

#for each file in the data source directory
for filename in original_files:
	#Skip non-text files
	if filename[-4:] != ".txt": 
		continue
	#read the text file and try to split it into speakers
	with open(join(SRC_PATH, filename), 'r') as file:
		print("Opened " + filename)
		transcript = re.sub(NEW_LINE, " ", file.read())
		speakers = re.split(SPEAKER, transcript)
		for s in speakers:
			anon_name = "{:03d}_{}.txt".format(next_file, filename[:-4])
			try:
				individual_file = open(join(DATA_PATH, anon_name), 'w')
				individual_file.write(s)
				individual_file.close()
			except:
				print("Couldn't save file " + anon_name)
			finally:
				next_file += 1
	print("{} files {} to {}".format(filename, first_file, next_file-1))
	first_file = next_file

print("Done")