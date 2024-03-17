import json
from typing import List
from datetime import datetime
from finder import Finder

# read json


def readJsonFile(fileName: str):
    with open(fileName) as json_file:
        return json.load(json_file)


# run GOAP algorithm
def run_goap(data):
    result: List[str] = []
    start = datetime.now()
    cP1 = Finder(data)
    result = cP1.execute()

    end = datetime.now()
    print(end - start)

    print(result)


run_goap(
    readJsonFile('actions.json')
)
