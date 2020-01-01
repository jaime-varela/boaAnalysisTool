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

class groupingAlgorithm(Enum):
    FirstNdigits = 1
    LastNdigits = 2
    StringSimilarity = 3
    NumericRemovalStringSimilarity = 4
    FirstNLastMdigits = 5

def removeNumerics(dataFrame, ColumnName):
    #TODO
    return

def removeNonAlpha(dataFrame, ColumnName):
    #TODO
    return


def textProcessDF(dataFrame, textProcessEnum, ColumnName, options={}):
    # using if else because python doesn't have enums
    if textProcessEnum == textProcessEnum.NumericRemoval:
        return removeNumerics(dataFrame, ColumnName)
    elif textProcessEnum == textProcessEnum.NonAlphabetCharRemoval:
        return removeNonAlpha(dataFrame, ColumnName)
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

def stringGroups():
    return 0.0


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

