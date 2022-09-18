# %%
from analasisAPI.fileLoader import LoadFile 
from analasisAPI.queries import filterDataFrameByRegex
from analasisAPI.queries import filterDataFrameByDate
from analasisAPI.queries import filterDataFrameByAmount
from analasisAPI.queries import queryBankDataFrame
from analasisAPI.plotUtilities import plotDataFrameTimeSeriesCol
import datetime


from analasisAPI.fileLoader import combineBOAfiles
# %%
# This should be the path to the file of your untouched BOA statement
filepath = "/home/jvarela/Documents/financial/stmt.csv"
# filepath = "sample.csv"


dataFrame = LoadFile(filepath)

regexDF = filterDataFrameByRegex(dataFrame,"uber")
#print(regexDF)

range1filter = filterDataFrameByDate(dataFrame,[datetime.datetime(2021,12,2),datetime.datetime(2022,12,22)])

# %%
dataFrame.dtypes

# %%
print(dataFrame.columns)
from classification.rule_based_classfier import classify_statement_from_rule_set

classified_df = classify_statement_from_rule_set(dataFrame)

classified_df.drop(columns=["Running Bal.","Amount"], inplace=True, errors="ignore")

classified_df.to_csv("test_classificatin.csv")


# %%
# deposit over 1k
# print(filterDataFrameByAmount(dataFrame,[1000.0,False]))


# uber costs in the last six months

queryCost = queryBankDataFrame(range1filter, "micro",dateRange=[datetime.datetime(2019,9,10),datetime.datetime(2019,12,10)])



# %%
