from analasisAPI.fileLoader import LoadFile 
from analasisAPI.queries import filterDataFrameByRegex
from analasisAPI.queries import filterDataFrameByDate
from analasisAPI.queries import filterDataFrameByAmount
from analasisAPI.queries import queryBankDataFrame
from analasisAPI.plotUtilities import plotDataFrameTimeSeriesCol
import datetime


from analasisAPI.fileLoader import combineBOAfiles

# This should be the path to the file of your untouched BOA statement
#filepath = "/home/jaimevrl/Documents/Finance/stmt.csv"
filepath = "sample.csv"


dataFrame = LoadFile(filepath)

# print(dataFrame.head())
regexDF = filterDataFrameByRegex(dataFrame,"uber")
#print(regexDF)

range1filter = filterDataFrameByDate(dataFrame,[datetime.datetime(2018,12,2),datetime.datetime(2019,12,22)])


range2filter = filterDataFrameByAmount(range1filter,[-100.0,True])

# print(range2filter)

# deposit over 1k
# print(filterDataFrameByAmount(dataFrame,[1000.0,False]))


# uber costs in the last six months
# print(queryBankDataFrame(dataFrame, "uber",dateRange=[datetime.datetime(2019,6,10),datetime.datetime(2019,12,10)]))

queryCost = queryBankDataFrame(range2filter, "micro",dateRange=[datetime.datetime(2019,9,10),datetime.datetime(2019,12,10)])

# print(queryCost)
# print(range2filter.to_string())
# plotDataFrameTimeSeriesCol(range2filter,'Date','Amount')
file1 = "/home/jaimevrl/Documents/Finance/stmt.csv"
# file2 = "/home/jaimevrl/Documents/Finance/stmt2.csv"
# outFile = "/home/jaimevrl/Documents/Finance/outTest.csv"

# combineBOAfiles(file1,file2,outFile)

dataFrame = LoadFile(file1)


from analasisAPI.subscriptionFinder import removeNumerics
from analasisAPI.subscriptionFinder import removeNonAlpha, removeNonAlphaNumeric
from analasisAPI.fileLoader import DESC_COL


# filteredDF = removeNonAlphaNumeric(dataFrame,DESC_COL)
# print(filteredDF)

# strval = "asdf23221sdaf"

# def trialVal(strv):
#     return ''.join(i for i in strv if not i.isdigit())

# newval = trialVal(strval)
# print(newval)

charVal = 4
str1 = "aaabbb"
str2 = "acabbb"
from analasisAPI.subscriptionFinder import NcharMatch, reverseNcharMatch, stringSimilarity
predVal = NcharMatch(str1,str2,nChars = charVal)
# print(predVal)
revpredval = reverseNcharMatch(str1,str2,nChars=charVal)
# print(revpredval)


print(stringSimilarity(str1,str2))
import Levenshtein

