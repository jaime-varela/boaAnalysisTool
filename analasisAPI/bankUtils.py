import pandas as pd
import numpy as np
import globals

def isChaseFile(in_filename):
    try:
        with open(in_filename, "r") as myfile:
            header = next(myfile).strip().split(",")
            if len(set([globals.column_names.CHASE_DATE_COL, globals.column_names.CHASE_DESC_COL, globals.column_names.CHASE_AMNT_COL, globals.column_names.CHASE_CAT_COL]).difference(set(header))) == 0:
                return True
    except:
        return False
    return False

def LoadChaseFile(in_filename):
    parse_dates = [0,1]
    dataFrame = pd.read_csv(in_filename,parse_dates=parse_dates)
    dataFrame[globals.column_names.DATE_COL] = dataFrame[globals.column_names.CHASE_DATE_COL]
    dataFrame[globals.column_names.DESC_COL] = dataFrame[globals.column_names.CHASE_DESC_COL].apply(lambda x: stripCommas(x))
    dataFrame[globals.column_names.AMNT_COL] = dataFrame[globals.column_names.CHASE_AMNT_COL]
    dataFrame[globals.column_names.CAT_COL] = dataFrame[globals.column_names.CHASE_CAT_COL]

    dataFrame[globals.column_names.BAL_COL] = np.cumsum(dataFrame[globals.column_names.AMNT_COL])

    return dataFrame[[globals.column_names.DATE_COL, globals.column_names.DESC_COL, globals.column_names.AMNT_COL, globals.column_names.BAL_COL, globals.column_names.CAT_COL]]


# Misc utils
def stripCommas(inputStr):
    return inputStr.replace(",","")


# BOA utils----------------
def isBoaDebitFile(in_filename):
    # TODO: not multi-national
    with open(in_filename) as myfile:
        head = [next(myfile) for x in range(6)] # first six line
    firstLineCondition = head[0].split(",")[0] == "Description"
    thirdLineCondition = head[2].split(",")[0] == "Total credits"
    fourthLineCondition= head[3].split(",")[0] == "Total debits"
    return firstLineCondition and thirdLineCondition and fourthLineCondition

def LoadBoaDebitFile(in_filename):
    parse_dates = [0]
    dataFrame = pd.read_csv(in_filename,skiprows=[0,1,2,3,4,5,7],parse_dates=parse_dates)
    dataFrame[globals.column_names.DATE_COL] = dataFrame[globals.column_names.BOA_DATE_COL]
    dataFrame[globals.column_names.DESC_COL] = dataFrame[globals.column_names.BOA_DESC_COL].apply(lambda x: stripCommas(x))
    dataFrame[globals.column_names.AMNT_COL] = dataFrame[globals.column_names.BOA_AMNT_COL].apply(lambda x: stripCommas(x))
    dataFrame[globals.column_names.BAL_COL] = dataFrame[globals.column_names.BOA_BAL_COL].apply(lambda x: stripCommas(x))
    dataFrame[globals.column_names.AMNT_COL] = dataFrame[globals.column_names.BOA_AMNT_COL].astype('float')
    dataFrame[globals.column_names.CAT_COL] = ""

    return dataFrame[[globals.column_names.DATE_COL, globals.column_names.DESC_COL, globals.column_names.AMNT_COL, globals.column_names.BAL_COL, globals.column_names.CAT_COL]]


def isBoaCreditFile(in_filename):
    return False

def LoadBoaCreditFile(in_filename):
    assert "not implemented"
    return
