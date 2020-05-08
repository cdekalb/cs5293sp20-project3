# Test to ensure that the json data is properly parsed

import project3
from project3 import main

def test_parseData():
    dataFile = 'yummlySample.json'
    data = project3.main.parseData(dataFile)
    assert len(data) == 452, "Sample file should have length 452"
