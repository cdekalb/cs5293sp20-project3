# Test to ensure that the data is converted to list of spacy objects

import project3
from project3 import main

def test_convertToFeatures():
    dataFile = 'yummlySample.json'
    data = project3.main.parseData(dataFile)
    docs = project3.main.convertToFeatures(data)
    assert len(docs[0].vector) == 300, "List must contain Spacy object with feature length of 300"
