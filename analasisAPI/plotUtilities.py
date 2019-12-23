import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

def groupDF(dataFrame, timeColName, dataColName):
    newDF = dataFrame.groupby([timeColName]).sum().reset_index()
    newDF = newDF[[timeColName,dataColName]]
    newDF.set_index(timeColName)
    newDF = newDF.sort_values(timeColName, ascending=True)
    return newDF

def groupDFAll(dataFrame, timeColName, dataColName,amntColName):
    newDF = dataFrame.groupby([timeColName]).sum().reset_index()
    newDF = newDF[[timeColName,dataColName,amntColName]]
    newDF.set_index(timeColName)
    newDF = newDF.sort_values(timeColName, ascending=True)
    return newDF


# TODO: more styling and crap
def plotDataFrameTimeSeriesCol(dataFrame, timeColName, dataColName, tickStyle = '*-', timesMinusOne = True):
    '''
        Will group the data by day and plot the result
    '''
    newDF = groupDF(dataFrame,timeColName,dataColName)
    factor = -1.0 if timesMinusOne else 1.0
    plt.plot(newDF[timeColName],factor * newDF[dataColName],tickStyle)
    plt.xticks(rotation='vertical')
    plt.show()


def plotBalanceAndCosts(dataFrame, timeColName, dataColName, amntColName, tickStyle = '*-', timesMinusOne = True,
                        CostTitle = "Costs per Day", BalanceTitle = "Balance over Time"):

    datefmt = dates.DateFormatter("%d-%b-%Y")
    fmt = lambda x,y : "{}, {:.5g}".format(datefmt(x), y)

    newDF = groupDFAll(dataFrame, timeColName,dataColName,amntColName)
    newDF = newDF[newDF[dataColName].apply(lambda x: x < 0.0)]
    factor = -1.0 if timesMinusOne else 1.0
    plt.figure(1)
    plt.subplot(211)
    plt.plot(newDF[timeColName],factor * newDF[dataColName],tickStyle)
    plt.title(CostTitle)
    plt.gca().format_coord = fmt
    # Figure 2
    plt.subplot(212)
    plt.plot(dataFrame[timeColName],dataFrame[amntColName])
    plt.title(BalanceTitle)
    plt.gca().format_coord = fmt
    plt.show()
