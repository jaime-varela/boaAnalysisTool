import pandas as pd
import functools
import re
import sys
# for small data sets using three function calls is sufficiently optimal

#constants in use to locate columns
from .fileLoader import BOA_DATE_COL
from .fileLoader import BOA_DESC_COL
from .fileLoader import BOA_AMNT_COL
from .fileLoader import BOA_BAL_COL 


def filterDataFrameColByPred(dataFrame, columnName,predicate):
    '''
        Input:
            dataFrame -> a pandas data frame
            columnName -> a column name
            predicate -> a unary predicate for the type in column
        Output:
            a dataframe containing only the rows which the predicate evaluated to true
    '''
    return dataFrame[dataFrame[columnName].apply(predicate)]

def lower_regex_filter_predicate(compareStr, regex):
    if compareStr:
        regexFound = re.search(regex.lower(),compareStr.lower()) # we lower both for case insensitivity
        if regexFound:
            return True
        else:
            return False
    else:
        return False

def filterDataFrameByRegex(dataFrame, regex):
    boundRegexFilter = lambda strVal: lower_regex_filter_predicate(strVal,regex)
    return filterDataFrameColByPred(dataFrame,BOA_DESC_COL,boundRegexFilter)

def filterDataFrameByRange(dataFrame,columnName, rangeArray):
    '''
        Input:
            dataFrame -> a data frame
            columnName -> column name
            rangeArray -> Two element array which is either [lowerBound,upperBound], [value,IsUpperBound (bool)].  For example [5.0, True] will give all 
                            rows whose value is less than 5.0.  Similarly [5.0,False] will give rows greater than 5.0. Note types must match
        Output:
            dataframe in range
    '''
    rangeLambda = []
    if type(rangeArray[1]) == type(True):
        if(rangeArray[1]):
            rangeLambda = lambda colVal: colVal <= rangeArray[0]
        else:
            rangeLambda = lambda colVal: colVal >= rangeArray[0]
    else:
        rangeLambda = lambda colVal: (colVal >= rangeArray[0]) and (colVal <= rangeArray[1])
    return filterDataFrameColByPred(dataFrame,columnName,rangeLambda)


def filterDataFrameByDate(dataFrame, dateRange):
    return filterDataFrameByRange(dataFrame,BOA_DATE_COL,dateRange)

# Note we keep the same methodology as BOA in that negative values are costs (sue use [-20.0,True] if you want all costs greater than 20 dollars)
def filterDataFrameByAmount(dataFrame, amountRange):
    return filterDataFrameByRange(dataFrame,BOA_AMNT_COL,amountRange)

def queryBankDataFrame(dataFrame, regex = "", dateRange = [], amountRange = []):
    finalDF = dataFrame
    if regex != "":
        finalDF = filterDataFrameByRegex(finalDF,regex)
    if dateRange != []:
        finalDF = filterDataFrameByDate(finalDF,dateRange)
    if amountRange != []:
        finalDF = filterDataFrameByAmount(finalDF,amountRange)
    if regex == "" and dateRange == [] and amountRange ==[]:
        assert('No range provided')
    return finalDF