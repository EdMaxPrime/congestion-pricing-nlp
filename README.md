# Overview
Analyzing public comments on the MTA's Central Business District tolling proposal. Evaluate segmentation of opinions for congestion pricing in New York City by identifying features which predispose someone to be for or against the plan.

Authors: Stacey Li and Max Zlotskiy

# Problem

Congestion pricing has become a hot topic in New York City. It’s a proposal to discourage drivers and alleviate NYC’s gridlocked streets and to raise money for the MTA. This will have huge ramifications for the most economically productive and densest metropolitan area in the country, so there will be many unforeseen ripple effects. Everyone has an opinion on how congestion pricing should be handled. We want to quantify the arguments. Is there widespread opposition to the plan from people of all walks of life, or are there just a few angry drivers? Is there widespread support for the plan, or is it limited to cyclists who live close to their jobs? Do people parrot the same talking points, or are they highlighting a multitude of indirect impacts on their lives?

# Data Sources

The MTA held live public meetings for each geographic area [linked here](https://new.mta.info/project/CBDTP/upcoming-meetings). We downloaded the transcripts from each meeting and split them up: one text file per speaker. Each speaker had 3 minutes.

- Residents below 60th street in Manhattan: https://youtu.be/LQl_5Z4ANZg
- Residents of the outer boroughs: https://www.youtube.com/watch?v=DpdU3tp4yN0
- Residents of New Jersey: https://www.youtube.com/watch?v=vCncmZrPjd8
- Residents of upstate (Dutchess, Orange, Putnam, Rockland, Westchester Counties): https://youtu.be/zbwCPk0AMDI
- Residents of Long Island: https://youtu.be/U2p3q9Z8Vvo
- Outer boroughs part 2: https://youtu.be/YiFUbRaYyKQ
- Connecticut: https://youtu.be/fcFSgY84m6o
- New Jersey Part 2: https://youtu.be/nDqOifk_MH4
- Upstate part 2: https://youtu.be/sQkbKvhDSv0
- Manhattan above 60th Street: https://youtu.be/_r0hER61xME

# How to Run It

## Virtual Environment

If you have python and pip on your system, you can make a virtual environment and then install the required libraries:
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Now download nltk's packages:
```
mkdir nltk_data
python setup.py
```

To deactivate the virtual environment, type `deactivate`. You can delete the environment with `rm -rf venv`

## Get data

After cloning this repository, populate the data directory.
```
python data_clean.py
```

## Feature Extraction

Then you can run feature extraction

```
python features/main.py
```

And it will generate a file called features.csv
