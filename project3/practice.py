import json
import spacy
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

def parseData(dataFile):
    # Parse through the data file
    with open(str(dataFile), 'r') as data_file:
        # Set the dictionary to an object called data
        data = json.load(data_file)
    return data

def getNumClusters(data):
    # Initialize an empty list to hold the all of the cuisines
    totalCuisines = []

    # Extract the cuisine type for each cuisine and append it to the list of total cuisines
    for i in range(len(data)):
        totalCuisines.append(data[i]['cuisine'])
    # Find the unique cuisines
    uniqueCuisines = set(totalCuisines)

    # Find the number of unique cuisines to use as the number of clusters
    numCuisines = len(uniqueCuisines)

    return numCuisines

def convertToFeatures(data):
    # Initialize an empty list to hold the total ingredients of each recipe
    totalIngredients = []

    # Parse through each recipe
    for i in range(len(data)):
        # Initialize an empty list to hold the ingredients for the specific recipe being observed
        tempIngredients = []

        # Parse through the characters of each ingredient
        for j in range(len(data[i]['ingredients'])):
            # Append the total string of the characters to tempIngredients
            tempIngredients.append(''.join(data[i]['ingredients'][j]))
        # Append the string of all the ingredients to totalIngredients
        totalIngredients.append(' '.join(tempIngredients))

    # Initialize an empty list to hold the spacy objects of each string
    docs = []

    # Parse through each list of ingredients
    for i in range(len(totalIngredients)):
        # Append the spacy objects to the docs list
        docs.append(nlp(totalIngredients[i]))
    
    return docs

def getBestSimilarities(userIngredients, docs):
    # Get the word2vec embedding of the user input
    userVector = nlp(userIngredients).vector

    # Initialize an empty list to hold the similarity values and indices of the recipes
    simValueAndIndex = []

    # Parse through the recipes
    for i in range(len(docs)):
        # Initialize an empty list to hold the similarity value and index of the current recipe
        # being compared
        tempSimValueAndIndex = []

        # Calculate the similarity values
        similarity = np.dot(userVector, docs[i].vector) / (np.linalg.norm(userVector) * np.linalg.norm(docs[i].vector))

        # Append the similarity value and the index of the current recipe to tempSimValueAndIndex
        tempSimValueAndIndex.append(similarity)
        tempSimValueAndIndex.append(i)

        # Append the current similarity value and index to the total list
        simValueAndIndex.append(tempSimValueAndIndex)

    # Sort based on the similarity values
    sortedSimilarities = sorted(simValueAndIndex, key = lambda x: x[0])[::-1]

    # Find the numClosestRecipes closest recipes
    bestSimilarities = sortedSimilarities[0:numClosestRecipes]

    return bestSimilarities

data = parseData('yummlySample.json')

# numClusters = getNumClusters(data)

# Load the large English spacy model
nlp = spacy.load('en_core_web_lg')

docs = convertToFeatures(data)

example = 'paprika cumin rice'

numClosestRecipes = 5

bestSimilarities = getBestSimilarities(example, docs)

print("Closest " + str(numClosestRecipes) + " recipes:", end = ' ')
for i in range(len(bestSimilarities)):
    print(" " + str(data[bestSimilarities[i][1]]["id"]) + " (" + str(round(bestSimilarities[i][0], 2)) + ")", end = ' ')

# print(0)