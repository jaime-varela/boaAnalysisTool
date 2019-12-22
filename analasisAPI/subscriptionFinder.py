import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# TODO: All of it
#
# maybe make a class?
#

# returns a numeric value between zero and one if a signal has a period
def isPeriodic(groupedDF, fourierThreshold):

    # Method 1 Auto correleation

    # Method 2 fourier transform analysis of some sort

    # TODO: find some average numerical measure and use an empirical threshold
    return 0.0


# returns the periods of the signal based on threshold conditions
def getPeriods(groupedDF, params):

    # FFT analysis and maybe autocorrelation
    return [0.0]

