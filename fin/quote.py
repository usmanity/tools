import sys
import json

data = sys.stdin.readline()

jsonData = json.loads(data)

print(jsonData['QuickQuoteResult']['QuickQuote']['FundamentalData']);

# print(json.dumps(jsonData['QuickQuoteResult'], indent=4, sort_keys=True))
