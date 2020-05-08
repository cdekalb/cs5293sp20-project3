# Project 3

Class:
CS 5293

Author:
Creighton DeKalb

# Project Summary

The purpose of this project is to recommend recipes based on what ingredients the user has on hand. The project does this by using word embeddings with word2vec and finds the most similar recipes to the user input by calculating the cosine similarity between the input ingredients and each recipe in the accompanying data file. This project used the spacy library to access the natural language processing (nlp) functionality as well as the sklearn library to access the CountVectorizer method in the feature_extraction.text package.

# Installing

In order to run this project, the user needs to install pipenv. This can be done in the command line using the command:

    pipenv install

The spaCy library also needs to be installed and can be done so with the command:

    pipenv install spacy

An additional library must be downloaded for spaCy to be able to work with the English language. It can be downloaded with the command:

    python -m spacy download en_core_web_lg

Additionally, the numpy and sklearn libraries are required for the project to run. These libraries can be downloaded similarly with the general command:

    python install <library>
    
# Prerequisites

To access the project, the user must navigate to the command line and run the command:

    git clone https://github.com/cdekalb/cs5293sp20-project3.git

# Tests

There are three test files in the project:

- test_parseData.py

The parse data test takes in a specific file that contains a subset of the yummly.json data. The test asserts that the length of the newly created dictionary object has the same number of entries as the sample file.

- test_convertToFeatures.py

The convert to features test takes uses the sample data from the parse data test and uses the spacy library to convert each list of ingredients into a document. The test asserts that the feature vector of the first document in the list of documents has length 300.

- test_getBestSimilarities.py

The get best similarities test takes a sample list of ingredients and the list of documents from the convert to features test and calculates the cosine similarity between the sample list of ingredients and each recipe. The test asserts that the first sublist in the created list of lists has length 2, corresponding to the similarity value and the index of the document being compared.

To run the tests, the user must navigate to the command line and run the command:

    pipenv run python -m pytest

# Deployment

The main file first parses through the yummly.json file to create a dictionary object. Then, it converts the string of ingredients for each recipe into feature vectors using Word2Vec. Then, it calculates the cosine similarity values between the feature of each recipe and the feature of the inputted ingredients and finds the closest 5 recipes to the inputted ingredients.

- parseData(dataFile):

The parseData method takes in the yummly.json file and reads its contents to a dictionary object.

- convertToFeatures(data):

The convertToFeatures method takes in the dictionary object from the parseData method, creates a single string of the joined ingredients for each recipe, then appends the nlp objects to a list.

- getBestSimilarities(userIngredients, docs):

The getBestSimilarities method takes in the string of the inputted ingredients and the list of nlp objects of the ingredients of each recipe. The method then calculates the cosine similarity of the feature vectors of the inputted ingredients and each recipe. Then the similarity scores are sorted and a list of lists where each sublist is the similarity score and the index of the given recipe is returned.

To run the code, navigate from the command line to the cs5293sp20-project3 directory in which all the project files exist. In the command line, enter the following:

    pipenv run python main.py --ingredient <ingredient1> --ingredient <ingredient2>

This command can have any number of ingredient arguments passed in. The command will run the main.py file using the inputted ingredients.

## Answers to Address the Rubric that Have Not Yet Been Answered

1: The text was turned into features by using the en_core_web_lg library to turn the string of all the ingredients per recipe into a spacy object. This was done with the following sections of code:

    nlp = spacy.load('en_core_web_lg')
    nlp(totalIngredients[i])

The object in the second line has a parameter called vector that is the word2vec transformation of the ingredients. This way of creating of the features was done because it most succinctly and accurately generates the word embeddings of the ingredients.

2: The code is currently set up to find the closest five clusters. This was decided upon because it gives the user enough information to provide variety in which recipes they choose, while not giving too much information so that it defeats the purpose of the recommender.

# Assumptions and Bugs

- The yummly.json file is the only file that should be used for this project.

- The inputted ingredients must be in English.