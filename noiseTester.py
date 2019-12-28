from analasisAPI.fileLoader import LoadFile 
from analasisAPI.queries import filterDataFrameByRegex
from analasisAPI.queries import filterDataFrameByDate
from analasisAPI.queries import filterDataFrameByAmount
from analasisAPI.queries import queryBankDataFrame
from analasisAPI.plotUtilities import plotDataFrameTimeSeriesCol
import datetime


from analasisAPI.fileLoader import combineBOAfiles
from analasisAPI.fileLoader import DATE_COL,AMNT_COL

file1 = "/home/jaimevrl/Documents/Finance/stmt.csv"
import matplotlib.pyplot as plt
import numpy as np
from pandas.plotting import autocorrelation_plot

dataFrame = LoadFile(file1)

dataFrame = filterDataFrameByRegex(dataFrame,"audible")
dataFrame = dataFrame.sort_values(by=DATE_COL)

import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

timeData = dataFrame[[DATE_COL,AMNT_COL]]
tseries = timeData.set_index(DATE_COL)
print(tseries)
# acorr = sm.tsa.stattools.acf(timeData)
from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_acf

tseries.plot()
plot_acf(tseries)
pyplot.show()

acorr = sm.tsa.stattools.acf(tseries,fft=False)
acorr_norm = acorr / acorr[0]
print(acorr_norm)