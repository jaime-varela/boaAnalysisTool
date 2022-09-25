# %%
from analasisAPI.subscriptionFinder import isDFweeklySchedule
from globals.column_names import BOA_DATE_COL
from analasisAPI.fileLoader import LoadFile 
from analasisAPI.queries import filterDataFrameByRegex
from analasisAPI.queries import filterDataFrameByDate
from analasisAPI.queries import filterDataFrameByAmount
from analasisAPI.queries import queryBankDataFrame
from analasisAPI.plotUtilities import plotDataFrameTimeSeriesCol
import datetime


from analasisAPI.bankUtils import combineBOAfiles
# %%
# This should be the path to the file of your untouched BOA statement
filepath = "/home/jvarela/Documents/financial/stmt.csv"
# filepath = "sample.csv"


dataFrame = LoadFile(filepath)

regexDF = filterDataFrameByRegex(dataFrame,"uber")
#print(regexDF)

range1filter = filterDataFrameByDate(dataFrame,[datetime.datetime(2021,12,2),datetime.datetime(2022,12,22)])

# %%
import pandas as pd
dataFrame.dtypes
val = pd.infer_freq(dataFrame[BOA_DATE_COL])
print(val)

# %%
idx = pd.date_range(start='2020/12/01', end='2020/12/30', periods=30)
pd.infer_freq(idx)
idx
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
# Analyze the data frame schedules
from analasisAPI.subscriptionFinder import textProcessDF, textProcessing,NcharMatch, binStringObjectsByPredicate
from analasisAPI.subscriptionFinder import extractDFfromStringIndexPairs, dataFrameSchedule, scheduleTypeEnum
from globals.column_names import BOA_DESC_COL


originalDataFrame = dataFrame
textProcessEnum = textProcessing.NonAlphaNumericCharRemoval
textProcessedDF = textProcessDF(dataFrame,textProcessEnum,BOA_DESC_COL)
processedDescriptionArray = textProcessedDF[BOA_DESC_COL].to_numpy()
binerPredicate = None
optionsDict = {'firstNchar': 6,
                'lastNchar': 4,
                'similarity': 80.0}

binerPredicate = lambda x,y: NcharMatch(x,y,nChars=optionsDict['firstNchar'])
binnedStringsAndIndeces = binStringObjectsByPredicate(processedDescriptionArray,binerPredicate)

scheduledDataFrames = []
for binEntry in binnedStringsAndIndeces:
    intermediateDataFrame = extractDFfromStringIndexPairs(originalDataFrame,binEntry)
    schedule = dataFrameSchedule(intermediateDataFrame)

    if schedule[0] != scheduleTypeEnum.NoSchedule:
        print(intermediateDataFrame.iloc[0])
        scheduledDataFrames.append((schedule,intermediateDataFrame))



# %%
