# Test to ensure that the similarities of the user input and recipes are calculated correctly

import project3
from project3 import main

def test_getBestSimilarities():
    dataFile = 'yummlySample.json'
    data = project3.main.parseData(dataFile)
    docs = project3.main.convertToFeatures(data)
    userIngredients = 'salt pepper oregano'
    bestSimilarities = project3.main.getBestSimilarities(userIngredients, docs)
    assert len(bestSimilarities[0]) == 2, "Each sublist must contain recipe index and similarity value"