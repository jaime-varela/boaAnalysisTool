import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# it has been decided that using auto-correlation and other tools is not beneficial for schedule finding for this data set type
# instead a custom condition set will be used

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



import string

def removeNumerics(dataFrame, ColumnName):    
    newDF = dataFrame
    newDF[ColumnName] = newDF[ColumnName].apply(lambda x: x.join(i for i in x if not i.isdigit()))
    return newDF

def removeNonAlpha(dataFrame, ColumnName):
    newDF = dataFrame
    newDF[ColumnName] = newDF[ColumnName].apply(lambda x: x.join(ch for ch in x if ch.isalpha()) )
    return newDF

def removeNonAlphaNumeric(dataFrame, ColumnName):
    newDF = dataFrame
    newDF[ColumnName] = newDF[ColumnName].apply(lambda x: x.join(ch for ch in x if ch.isalnum()) )
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

# Rough algorithm sketch
# 1.) process each description element with a text processing algorithm
# 2.) put each row of the data frame into a bin corresponding to a predicate condition (look up binning based on binary predicate)
# 3.) for each bin, determine if the data is scheduled
# 4.) if a bin is scheduled determine its schedule and place a representative element in the display data frame
# 5.) if a bin is not scheduled do nothing
#
# The display data frame consists of the following columns [Representative Description, Avg. Cost, Schedule (Daily,weekly, or monthly), Occurence (days of week, day of week, or day of month)]
# bi-monthly might be tricky and so is non-approximate schedules.


# binning predicates
def NcharMatch(str1, str2, searchIndexStart = 0, nChars = 6):
    #TODO: assert check on params
    compareStr1 = str1[searchIndexStart:searchIndexStart + nChars - 1]
    compareStr2 = str2[searchIndexStart:searchIndexStart + nChars - 1]
    return compareStr1.lower() == compareStr2.lower()

def reverseNcharMatch(str1,str2, reverseIndexStart = 0, nChars = 6):
    #TODO: assert check on params
    startIndex1 = len(str1) - (reverseIndexStart + nChars)
    startIndex2 = len(str2) - (reverseIndexStart + nChars)
    endIndex1 = startIndex1 + nChars
    endIndex2 = startIndex2 + nChars
    compareStr1 = str1[startIndex1:endIndex1]
    compareStr2 = str2[startIndex2:endIndex2]
    return compareStr1.lower() == compareStr2.lower()

import Levenshtein

def stringSimilarity(str1,str2 , threshold = 0.85):
    len1 = len(str1)
    len2 = len(str2)
    return (Levenshtein.distance(str1,str2) / max(len1,len2)) > 0.85


# Binning algorithm:

# will have to use an O(N^2) algorithm and measure it for long term viability.
# The O(N^2) algorithm should be find withing the low thousands but will inevitably fail for
# the millions of entries.  Depending on how long it takes for bank entries to grow
# this may not be a problem

# It is likely that case by case versions of each binning scenario will
# have lower complexity algorithms.  Any binning where an ordering relation 
# is preserved can be easily solved.  The string similarity algorithm might be the trickiest.

def binStringObjectsByPredicate(stringArray, predicate):
    '''
        Very dumb O(N^2) algorithm which returns an array of arrays of elements such that each sub array
        has all elements with true predicates.
    '''    
    retVal = []
    counter = 0
    predicateValueFound = False
    for strval in stringArray:
        if counter == 0:
            retVal.append([strval])
            counter += 1
        predicateValueFound = False
        for trialStr in retVal:
            if predicateValueFound:
                break
            if predicate(strval,trialStr[0]):
                trialStr.append(strval)
                predicateValueFound = True
        if not predicateValueFound and counter != 0:
            retVal.append([strval])
            counter += 1

    return retVal






# returns a numeric value between zero and one if a signal has a period
def dataFrameSchedule(groupedDF, fourierThreshold):

    # Method 1 Auto correleation

    # Method 2 fourier transform analysis of some sort

    # TODO: find some average numerical measure and use an empirical threshold
    return 0.0


# returns the periods of the signal based on threshold conditions
def getPeriods(groupedDF, params):

    # FFT analysis and maybe autocorrelation
    return [0.0]

