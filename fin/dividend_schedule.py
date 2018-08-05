import sys
import datetime
import time

#
def removeNewLines(input):
    if '\n' in input:
        return input.replace('\n', '')

def getTimestamp(humanReadableDate):
    return time.mktime(datetime.datetime.strptime(humanReadableDate, "%Y-%m-%d").timetuple())

# this line will read in any info piped into this script
data = sys.stdin.readlines()

# for making sure I'm seeing things inside this script
print("-------PRINTING DATA-----------")

quoteList = []

# remove the first element in the data which is the headers for the table
data.pop(0)

for line in data:
    splitPair = line.split(',')
    # convert human date to unix timestamp
    splitPair[0] = int(getTimestamp(splitPair[0]))
    # the price comes back with a new line \n character in it
    splitPair[1] = removeNewLines(splitPair[1])
    quoteList.append(splitPair)


sortedQuotes = sorted(quoteList, key = lambda x: x[0])

for quote in sortedQuotes:
    quote[0] = datetime.datetime.fromtimestamp(int(quote[0])).strftime('%Y-%B')

for quote in sortedQuotes[::-1]:
    splitDate = quote[0].split('-')
    splitDate[1] = splitDate[1].ljust(10)
    print(splitDate[0] + " - " + splitDate[1] + ": $" + quote[1])
