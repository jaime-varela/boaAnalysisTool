import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
from globals.column_names import DATE_COL, DESC_COL, AMNT_COL
register_matplotlib_converters()

# it has been decided that using auto-correlation and other tools is not beneficial for schedule finding for this data set type
# instead a custom condition set will be used

# Rough algorithm sketch
# 1.) process each description element with a text processing algorithm
# 2.) put each row of the data frame into a bin corresponding to a predicate condition (look up binning based on binary predicate)
# 3.) for each bin, determine if the data is scheduled
# 4.) if a bin is scheduled determine its schedule and place a representative element in the display data frame
# 5.) if a bin is not scheduled do nothing
#
# The display data frame consists of the following columns [Representative Description, Avg. Cost, Schedule (Daily,weekly, or monthly), Occurence (days of week, day of week, or day of month)]
# bi-monthly might be tricky and so is non-approximate schedules.


# ---------------- Enums -----------------------------------------------------------------

from enum import Enum

class textProcessing(Enum):
    NumericRemoval = 1
    NonAlphabetCharRemoval = 2
    NonAlphaNumericCharRemoval = 3

class groupingAlgorithm(Enum):
    FirstNdigits = 1
    LastNdigits = 2
    StringSimilarity = 3
    FirstNandLastMdigits = 4

class scheduleTypeEnum(Enum):
    Daily = 1
    Weekly = 2
    Monthly = 3
    NoSchedule = 4


import string

# ----------------------- Text processors --------------------------------------

def removeNumerics(dataFrame, ColumnName):    
    newDF = dataFrame
    newDF[ColumnName] = newDF[ColumnName].apply(lambda x: ''.join(i for i in x if not i.isdigit()))
    return newDF

def removeNonAlpha(dataFrame, ColumnName):
    newDF = dataFrame
    newDF[ColumnName] = newDF[ColumnName].apply(lambda x: ''.join(ch for ch in x if ch.isalpha()) )
    return newDF

def removeNonAlphaNumeric(dataFrame, ColumnName):
    newDF = dataFrame
    newDF[ColumnName] = newDF[ColumnName].apply(lambda x: ''.join(ch for ch in x if ch.isalnum()) )
    return newDF

def textProcessDF(dataFrame, textProcessEnum, ColumnName, options={}):
    # using if else because python doesn't have enums
    if textProcessEnum == textProcessEnum.NumericRemoval:
        return removeNumerics(dataFrame, ColumnName)
    elif textProcessEnum == textProcessEnum.NonAlphabetCharRemoval:
        return removeNonAlpha(dataFrame, ColumnName)
    elif textProcessEnum == textProcessEnum.NonAlphabetCharRemoval:
        return removeNonAlphaNumeric(dataFrame, ColumnName)
    else:
        return dataFrame

# --------------------- String binary predicates ------------------------

# binning predicates
def NcharMatch(str1, str2, searchIndexStart = 0, nChars = 6):
    #TODO: assert check on params
    compareStr1 = str1[searchIndexStart:searchIndexStart + nChars]
    compareStr2 = str2[searchIndexStart:searchIndexStart + nChars]
    return compareStr1.lower() == compareStr2.lower()

def reverseNcharMatch(str1,str2, reverseIndexStart = 0, nChars = 4):
    #TODO: assert check on params
    startIndex1 = len(str1) - (reverseIndexStart + nChars)
    startIndex2 = len(str2) - (reverseIndexStart + nChars)
    endIndex1 = startIndex1 + nChars
    endIndex2 = startIndex2 + nChars
    compareStr1 = str1[startIndex1:endIndex1]
    compareStr2 = str2[startIndex2:endIndex2]
    return compareStr1.lower() == compareStr2.lower()

import Levenshtein

def stringSimilarity(str1,str2 , threshold = 0.80):
    len1 = len(str1)
    len2 = len(str2)
    distMeasure = abs(1-(Levenshtein.distance(str1,str2) / max(len1,len2)) )
    return distMeasure > threshold


# Binning algorithm:

# will have to use an O(N^2) algorithm and measure it for long term viability.
# The O(N^2) algorithm should be fine withing the low thousands but will inevitably fail for
# the millions of entries.  Depending on how long it takes for bank entries to grow
# this may not be a problem

# It is likely that case by case versions of each binning scenario will
# have lower complexity algorithms.  Any binning where an ordering relation 
# is preserved can be easily solved.  The string similarity algorithm might be the trickiest.Schedule
def binStringObjectsByPredicate(stringArray, predicate):
    '''
        Very dumb O(N^2) algorithm which returns an array of arrays of the form:
        
        [[{str11,ind11},...],[{str21,ind21},...]].

        Such that predicate(strij,strik) = True and predicate(strij,strlm) = False for i != l.  
        The index for each pair in an array corresponds to the strings index in the original array.
    '''    

    retVal = []
    counter = 0
    predicateValueFound = False
    for strval in stringArray:
        if counter == 0:
            retVal.append([(strval,counter)])
            counter += 1
            continue
        predicateValueFound = False
        for trialStrArray in retVal:
            representativeString = trialStrArray[0][0]
            if predicateValueFound:
                break
            if predicate(strval,representativeString):
                trialStrArray.append((strval,counter))
                predicateValueFound = True
        if not predicateValueFound and counter != 0:
            retVal.append([(strval,counter)])
        
        counter += 1

    return retVal



def averageDFTimeDifference(groupedDF, timeColName):
    newDF = groupedDF.sort_values(timeColName, ascending=True)
    newDF = newDF[timeColName].diff()
    return newDF.mean().total_seconds()



#----------------------- Schedule Predicates ------------------------------------------------------

# groupedDF is assumed to be sorted
#TODO : refactor out the code duplication in the count predicates
def isDFcountInDailyRange(groupedDF,timeColName):
    firstRow = groupedDF.iloc[0]
    lastRow = groupedDF.iloc[-1]
    startDate = firstRow[timeColName]
    endDate = lastRow[timeColName]
    timeRange = (endDate - startDate)
    totalSeconds = timeRange.total_seconds()
    NumberOfDays = totalSeconds / (24*60*60)
    NumberOfWeeks = NumberOfDays / 7

    nMin = 2 * NumberOfWeeks # twice a week
    nMax = NumberOfDays # seven days a week

    Nentries = len(groupedDF[timeColName].unique())
    if Nentries >= nMin and Nentries <= nMax:
        return True
    return False



def isDFdailySchedule(groupedDF,timeColName):
    timeDiff = averageDFTimeDifference(groupedDF, timeColName)
    if not isDFcountInDailyRange(groupedDF,timeColName):
        return False

    oneday = 24 * 60 * 60
    fivedays = 5*oneday
    if timeDiff > fivedays:
        return False

    return True


def isDFcountInWeeklyRange(groupedDF,timeColName):
    firstRow = groupedDF.iloc[0]
    lastRow = groupedDF.iloc[-1]
    startDate = firstRow[timeColName]
    endDate = lastRow[timeColName]
    timeRange = (endDate - startDate)
    totalSeconds = timeRange.total_seconds()
    NumberOfDays = totalSeconds / (24*60*60)
    NumberOfWeeks = NumberOfDays / 7


    weekMinFudgeFactor = 0.85
    weekMaxFudgeFactor = 1.1
    nMin = weekMinFudgeFactor * NumberOfWeeks # twice a week
    nMax = weekMaxFudgeFactor * NumberOfWeeks # seven days a week

    Nentries = len(groupedDF[timeColName].unique())
    if Nentries >= nMin and Nentries <= nMax:
        return True
    return False


def isDFweeklySchedule(groupedDF,timeColName):
    timeDiff = averageDFTimeDifference(groupedDF, timeColName)
    oneday = 24 * 60 * 60
    sevendays = 7*oneday
    fudgeFactor = 1.1

    if not isDFcountInWeeklyRange(groupedDF,timeColName):
        return False

    if timeDiff > fudgeFactor *sevendays:
        return False
    if isDFdailySchedule(groupedDF,timeColName):
        return False    
    return True

def isDFcountInMonthlyRange(groupedDF,timeColName):
    firstRow = groupedDF.iloc[0]
    lastRow = groupedDF.iloc[-1]
    startDate = firstRow[timeColName]
    endDate = lastRow[timeColName]
    timeRange = (endDate - startDate)
    totalSeconds = timeRange.total_seconds()
    NumberOfDays = totalSeconds / (24*60*60)
    NumberOfWeeks = NumberOfDays / 7


    monthMinFudgeFactor = 0.85
    monthMaxFudgeFactor = 1.1
    nMin = monthMinFudgeFactor * (NumberOfWeeks / 4.0)# twice a week
    nMax = monthMaxFudgeFactor * (NumberOfWeeks / 4.0)# seven days a week

    Nentries = len(groupedDF[timeColName].unique())
    if Nentries >= nMin and Nentries <= nMax:
        return True
    return False



def isDFMonthlySchedule(groupedDF,timeColName):
    timeDiff = averageDFTimeDifference(groupedDF, timeColName)
    oneday = 24 * 60 * 60
    month = 30*oneday
    fudgeFactor = 1.2
    if not isDFcountInMonthlyRange(groupedDF,timeColName):
        return False

    if timeDiff > fudgeFactor * month:
        return False
    if isDFdailySchedule(groupedDF,timeColName) or isDFweeklySchedule(groupedDF,timeColName):
        return False
    return True

#----------------------- Schedulers ------------------------------------------------------


def dailyDFSchedule(groupedDF,timeColName):
    if not isDFdailySchedule(groupedDF,timeColName):
        return {}
    daysOfWeek = groupedDF[timeColName].apply(lambda x: x.weekday())
    daysOfWeek = daysOfWeek.unique()
    #TODO: remove sporadic days from data
    return daysOfWeek

def weeklyDFSchedule(groupedDF,timeColName):
    if not isDFweeklySchedule(groupedDF,timeColName):
        return {}
    dayOfWeek = groupedDF[timeColName].apply(lambda x: x.weekday())
    return dayOfWeek.mode().iloc[0] # FIXME: right now just picking first one

def monthlyDFSchedule(groupedDF,timeColName):
    if not isDFMonthlySchedule(groupedDF,timeColName):
        return {}
    dayOfMonth = groupedDF[timeColName].apply(lambda x: int(x.day))
    # NOTE: the days of the month are returned as negative in order to discriminate against
    # weekly values without needing the schedule enum.
    return (-1) * dayOfMonth.mode().iloc[0]


# returns a numeric value between zero and one if a signal has a period
def dataFrameSchedule(groupedDF):
    if len(groupedDF.index) <= 2:
        return (scheduleTypeEnum.NoSchedule,[])
    # get the average of difference in time of the data frame
    isDaily = isDFdailySchedule(groupedDF, DATE_COL)
    
    isWeekly = isDFweeklySchedule(groupedDF,DATE_COL)

    isMonthly = isDFMonthlySchedule(groupedDF,DATE_COL)

    if isDaily:
        return (scheduleTypeEnum.Daily,dailyDFSchedule(groupedDF,DATE_COL))
    elif isWeekly:
        return (scheduleTypeEnum.Weekly,weeklyDFSchedule(groupedDF,DATE_COL))
    elif isMonthly:
        return (scheduleTypeEnum.Monthly,monthlyDFSchedule(groupedDF,DATE_COL))
    else:
        return (scheduleTypeEnum.NoSchedule,[])


# ------------------------- Utilities ---------------------------------------------

def extractDFfromStringIndexPairs(dataFrame, stringIndexPairs):
    indList = []
    for pair in stringIndexPairs:
        indList.append(pair[1])
    return dataFrame.iloc[indList,:]


# ------------------------- Implementation of schedulers --------------------------

# combine all functions to get schedules
def getSchedules(dataFrame, textProcessEnum, groupAlgoEnum ,optionsDict):

    originalDataFrame = dataFrame
    textProcessedDF = textProcessDF(dataFrame,textProcessEnum,DESC_COL)
    processedDescriptionArray = textProcessedDF[DESC_COL].to_numpy()
    binerPredicate = None
    # TODO: pass in options
    if groupAlgoEnum == groupingAlgorithm.FirstNdigits:
        binerPredicate = lambda x,y: NcharMatch(x,y,nChars=optionsDict['firstNchar'])
    elif groupAlgoEnum == groupingAlgorithm.LastNdigits:
        binerPredicate = lambda x,y: reverseNcharMatch(x,y,nChars=optionsDict['lastNchar'])
    elif groupAlgoEnum == groupingAlgorithm.StringSimilarity:
        binerPredicate = lambda x,y: stringSimilarity(x,y,threshold=optionsDict['similarity'])
    else:
        return []
    binnedStringsAndIndeces = binStringObjectsByPredicate(processedDescriptionArray,binerPredicate)

    scheduledDataFrames = []
    for binEntry in binnedStringsAndIndeces:
        intermediateDataFrame = extractDFfromStringIndexPairs(originalDataFrame,binEntry)
        schedule = dataFrameSchedule(intermediateDataFrame)

        if schedule[0] != scheduleTypeEnum.NoSchedule:
            scheduledDataFrames.append((schedule,intermediateDataFrame))
    return scheduledDataFrames

#TODO: get rid of this global and update makeScheduleDFdisplayable
SCHEDULE_COLUMNS = ['Description','Frequency','Avg. Cost','Schedule']

def getRepresentativeDFfromSchedules(scheduledDataFrames):
    columns = SCHEDULE_COLUMNS
    dataValues = []
    for scheduleEntry in scheduledDataFrames:
        description = scheduleEntry[1][DESC_COL].iloc[0]
        datum = [description,scheduleEntry[0][0],scheduleEntry[1][AMNT_COL].mean(),scheduleEntry[0][1]]
        dataValues.append(datum)
    return pd.DataFrame(dataValues,columns=columns)



        


