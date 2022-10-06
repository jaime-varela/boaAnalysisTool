import numpy as np
import pandas as pd
from .bankUtils import isBoaDebitFile, isChaseFile ,isBoaCreditFile
from .bankUtils import LoadBoaCreditFile,LoadBoaDebitFile,LoadChaseFile


def npNum2Str(number):
    return str( np.round(number,decimals = 2) ) 



bankPredicateLoadActionPairs = [(isBoaDebitFile,LoadBoaDebitFile),
    (isChaseFile,LoadChaseFile),(isBoaCreditFile,LoadBoaCreditFile)]

# the current BOA file has six useless rows so we do not read those
# TODO: make this more robust for different bank formats
def LoadFile(filePath):
    '''
        Input:
            filepath -> path to BOA csv file
        Output: 
            pandas dataframe
    '''
    for predicate,loader in bankPredicateLoadActionPairs:
        if predicate(filePath):
            return loader(filePath)



