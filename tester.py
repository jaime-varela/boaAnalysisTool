from analasisAPI.fileLoader import LoadFile 
from analasisAPI.queries import filterDataFrameByRegex
from analasisAPI.queries import filterDataFrameByDate
from analasisAPI.queries import filterDataFrameByAmount
from analasisAPI.queries import queryBankDataFrame
from analasisAPI.plotUtilities import plotDataFrameTimeSeriesCol
import datetime


# This should be the path to the file of your untouched BOA statement
filepath = "/home/jaimevrl/Documents/Finance/stmt.csv"

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

print(queryCost)
print(range2filter.to_string())
plotDataFrameTimeSeriesCol(range2filter,'Date','Amount')