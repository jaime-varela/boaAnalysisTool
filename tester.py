# %%
from analasisAPI.subscriptionFinder import isDFweeklySchedule
from globals.column_names import DATE_COL
from analasisAPI.fileLoader import LoadFile 
from analasisAPI.queries import filterDataFrameByRegex
from analasisAPI.queries import filterDataFrameByDate
from analasisAPI.queries import filterDataFrameByAmount
from analasisAPI.queries import queryBankDataFrame
from analasisAPI.plotUtilities import plotDataFrameTimeSeriesCol
import datetime

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
val = pd.infer_freq(dataFrame[DATE_COL])
print(val)

# %%
idx = pd.date_range(start='2020/12/01', end='2020/12/30', periods=30)
pd.infer_freq(idx)
idx
# %%
print(dataFrame.columns)
from classification.rule_based_classfier import classify_statement_from_rule_set

classified_df = classify_statement_from_rule_set(dataFrame)

classified_df.drop(columns=["Running Bal."], inplace=True, errors="ignore")

classified_df = classified_df.drop_duplicates()

classified_df.to_csv("training_data.csv",index=False)

# %% Naive bayes classifier
# from classification.naive_bayes_classifier import classify_using_naive_bayes
# bayes_classified_df = classify_using_naive_bayes(dataFrame,training_file="/home/jvarela/Dropbox/software/bankStatementClassification/boaAnalysisTool/training_data.csv")
# from globals.column_names import BAYES_TRAINING_DESCRIPTION_COL
# training_df = pd.read_csv("/home/jvarela/Dropbox/software/bankStatementClassification/boaAnalysisTool/training_data.csv")
# training_df.head(33)

# for ind,row in training_df.iterrows():
#     print(row)
#     des= row[BAYES_TRAINING_DESCRIPTION_COL]
# bayes_classified_df.drop(columns=["Running Bal.","Amount","Date"], inplace=True, errors="ignore")

# bayes_classified_df = bayes_classified_df.drop_duplicates()

# bayes_classified_df.to_csv("classified_data.csv",index=False)

# %%
# deposit over 1k
# print(filterDataFrameByAmount(dataFrame,[1000.0,False]))


# uber costs in the last six months

# queryCost = queryBankDataFrame(range1filter, "micro",dateRange=[datetime.datetime(2019,9,10),datetime.datetime(2019,12,10)])



# %%
# Analyze the data frame schedules
from analasisAPI.subscriptionFinder import textProcessDF, textProcessing,NcharMatch, binStringObjectsByPredicate
from analasisAPI.subscriptionFinder import extractDFfromStringIndexPairs, dataFrameSchedule, scheduleTypeEnum
from globals.column_names import DESC_COL


originalDataFrame = dataFrame
textProcessEnum = textProcessing.NonAlphaNumericCharRemoval
textProcessedDF = textProcessDF(dataFrame,textProcessEnum,DESC_COL)
processedDescriptionArray = textProcessedDF[DESC_COL].to_numpy()
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
classified_df.head()

# %%
from classification.classification_report_utils import classification_pi_chart
classification_pi_chart(classified_df)
# %%


# %%
from datetime import date

d0 = date(2008, 8, 18)
d1 = date(2008, 9, 21)
delta = d1 - d0
print(delta.days)

# %%
dayOfWeek_enum = 3
first_week_day = 4
for ind in range(16):
    print((ind - (dayOfWeek_enum - first_week_day) ) % 7)
# %%
from analasisAPI.dateUtils import WeekDay, day_array_for_weekly_schedule

day_array_for_weekly_schedule(d0,d1,WeekDay.MONDAY)
# %%
d0 < d1
# %%
