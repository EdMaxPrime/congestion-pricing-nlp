from os import listdir, getcwd, mkdir
from os.path import join, dirname, exists
import re

DATA_PATH = "data"
SPEAKER = re.compile("===")
# === allows to compare regexp to string
NEW_LINE = re.compile("\n\n")
# \n\n makes a newline

original_files = listdir(getcwd())
cwd = getcwd() 
# listdir returns list containing the names of the entries in the directory given the path
# getcwd copies the absolute pathname of the current working directory  
next_file = 0
first_file = 0

# create data directory
path = join(cwd, DATA_PATH)
if not exists(path):
	mkdir(path)

#for each file in this directory
for filename in original_files:
	#Skip non-text files
	if filename[-4:] != ".txt": #if the last 4 chars in filename are not .txt
		continue
	#read the text file and try to split it
	with open(filename, 'r') as file:
		print("Opened " + filename)
		transcript = re.sub(NEW_LINE, " ", file.read())
		speakers = re.split(SPEAKER, transcript)
		for s in speakers:
			anon_name = "{:03d}.txt".format(next_file)
			try:
				individual_file = open(join(path, anon_name), 'w')
				individual_file.write(s)
				individual_file.close()
			except:
				print("Couldn't save file " + anon_name)
			finally:
				next_file += 1
	print("{} files {} to {}".format(filename, first_file, next_file-1))
	first_file = next_file

print("Done")