import numpy as np
import pandas as pd
from globals.column_names import BOA_BAL_COL,BOA_AMNT_COL,BOA_DATE_COL,BOA_DESC_COL,BOA_SUMMARY_CONST
from .bankUtils import isBoaFile, isChaseFile ,isBoaCreditFile
from .bankUtils import LoadBoaCreditFile,LoadBoaFile,LoadChaseFile


def npNum2Str(number):
    return str( np.round(number,decimals = 2) ) 



bankPredicateLoadActionPairs = [(isBoaFile,LoadBoaFile),
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



