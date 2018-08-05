import sys
import json

data = sys.stdin.readline()

jsonData = json.loads(data)

class Quote():
    def __init__(self, quoteData):
        self.quoteData = quoteData
        self.fundamentalData = quoteData['QuickQuoteResult']['QuickQuote']['FundamentalData']
        self.setupData(quoteData)

    def getRawData(self):
        return json.dumps(self.quoteData['QuickQuoteResult'], indent=4, sort_keys=True)

    def getStats(self):
        return json.dumps(self.fundamentalData)

    def setupData(self, data):
        self.usefulData = {}
        print(data);

q = Quote(jsonData)
# print(q.getStats())
