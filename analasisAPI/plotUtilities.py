import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# TODO: more styling and crap
def plotDataFrameTimeSeriesCol(dataFrame, timeColName, dataColName, tickStyle = '*-', timesMinusOne = True):
    '''
        Will group the data by day and plot the result
    '''
    newDF = dataFrame.groupby([timeColName]).sum().reset_index()
    newDF = newDF[[timeColName,dataColName]]
    newDF.set_index(timeColName)
    newDF = newDF.sort_values(timeColName, ascending=True)
    factor = -1.0 if timesMinusOne else 1.0
    plt.plot(newDF[timeColName],factor * newDF[dataColName],tickStyle)
    plt.xticks(rotation='vertical')
    plt.show()

