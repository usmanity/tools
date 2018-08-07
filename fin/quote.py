import sys
import json

data = sys.stdin.readline()

if len(data) > 1:
    jsonData = json.loads(data)
else:
    with open('cached/orc_quote.txt', 'r') as file:
        data = file.readlines()
        jsonData = json.loads(data[0])

class Quote():
    def __init__(self, quoteData):
        self.quoteData = quoteData
        self.fundamentalData = quoteData['QuickQuoteResult']['QuickQuote']['FundamentalData']
        self.setupData(self.fundamentalData)

    def getRawData(self):
        return json.dumps(self.quoteData['QuickQuoteResult'], indent=4, sort_keys=True)

    def getStats(self):
        return json.dumps(self.usefulData)

    def setupData(self, data):
        self.usefulData = {}
        self.usefulData['price'] = round(float(data['MPreviousClose']), 2)

q = Quote(jsonData)
print(q.getStats())
