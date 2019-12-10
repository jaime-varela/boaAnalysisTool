from analasisAPI.fileLoader import LoadFile 
from analasisAPI.queries import filterDataFrameByRegex
from analasisAPI.queries import filterDataFrameByDate
from analasisAPI.queries import filterDataFrameByAmount
from analasisAPI.queries import queryBankDataFrame
import datetime


# This should be the path to the file of your untouched BOA statement
filepath = "/home/jaimevrl/Documents/Finance/stmt.csv"

dataFrame = LoadFile(filepath)

# print(dataFrame.head())
regexDF = filterDataFrameByRegex(dataFrame,"uber")
#print(regexDF)

range1filter = filterDataFrameByDate(regexDF,[datetime.datetime(2018,12,2),datetime.datetime(2019,12,22)])


range2filter = filterDataFrameByAmount(range1filter,[-20.0,True])

# print(range2filter)

# deposit over 1k
# print(filterDataFrameByAmount(dataFrame,[1000.0,False]))


# uber costs in the last six months
print(queryBankDataFrame(dataFrame, "uber",dateRange=[datetime.datetime(2019,9,10),datetime.datetime(2019,12,10)]))

uberCost = queryBankDataFrame(dataFrame, "uber",dateRange=[datetime.datetime(2019,9,10),datetime.datetime(2019,12,10)])

print(uberCost.sum())