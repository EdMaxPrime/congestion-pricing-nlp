from os import getcwd, listdir, sep, pardir
from os.path import join, normpath
import re
# from nltk.corpus import stopwords


def preprocess(speaker):
    #remove punctuation
    speaker = re.sub(r'[^\w\s]', '', speaker)
    #split text
    speaker = speaker.split()
    #remove stopwords
    # stop_words = set(stopwords.words("english"))
    # speaker = [word for word in speaker if word not in stop_words]
    
    return speaker

def avg_length(speaker):
    print(speaker)
    avg = sum(len(word) for word in speaker) / len(speaker)
    return avg

def avg_length_without_filler(speaker):
    without_uh = list(filter(lambda a: a != 'uh', speaker))
    without_um = list(filter(lambda a: a != 'uh', without_uh))
    avg_without_filler = sum(len(word) for word in without_um) / len(without_um)
    return avg_without_filler


def filler_count(speaker):
    # instances = speaker.count('\s*u[h|m]\s*')
    instances = 0
    # speaker = speaker.split()
    for word in speaker: 
        # print(word)
        if word == 'uh' or word == 'um':
            instances += 1
    return instances

def read_file():
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
                print(filename)
                print(speaker)
    
            