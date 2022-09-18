import numpy as np
import pandas as pd

def npNum2Str(number):
    return str( np.round(number,decimals = 2) ) 


DATE_COL = 'Date'
DESC_COL = 'Description'
AMNT_COL = 'Amount'
BAL_COL = 'Running Bal.'

SUMMARY_CONST = 'Summary Amt.'


def stripCommas(inputStr):
    return inputStr.replace(",","")


# the current BOA file has six useless rows so we do not read those
# TODO: make this more robust for different bank formats
def LoadFile(filePath):
    '''
        Input:
            filepath -> path to BOA csv file
        Output: 
            pandas dataframe
    '''
    parse_dates = [0]
    dataFrame = pd.read_csv(filePath,skiprows=[0,1,2,3,4,5,7],parse_dates=parse_dates)
    dataFrame[DESC_COL] = dataFrame[DESC_COL].apply(lambda x: stripCommas(x))
    dataFrame[AMNT_COL] = dataFrame[AMNT_COL].apply(lambda x: stripCommas(x))
    dataFrame[BAL_COL] = dataFrame[BAL_COL].apply(lambda x: stripCommas(x))
    dataFrame[AMNT_COL] = dataFrame[AMNT_COL].astype('float')
    dataFrame[BAL_COL] = dataFrame[BAL_COL].astype('float')    
    return dataFrame



def combineBOAfiles(file1,file2,outFile):
    '''
        Input:
            file1 : first boa file
            file2 : second boa file
            outFile: output file string
    '''
    df1 = LoadFile(file1)
    df2 = LoadFile(file2)
    unionDataFrame = pd.concat([df1, df2]).drop_duplicates()
    unionDataFrame.sort_values(by=[DATE_COL])
    transactionCount = unionDataFrame[DATE_COL].count()
    preAmbleRows = []
    preAmbleRows.append(DESC_COL+',,'+SUMMARY_CONST+"," +"\n")
    preAmbleRows.append("Beginning balance as of " + str(unionDataFrame[DATE_COL].iloc[0]) +",," + npNum2Str(unionDataFrame[BAL_COL].iloc[0]) + "," +"\n")
    preAmbleRows.append(",,," +"\n")
    preAmbleRows.append(",,," +"\n")
    preAmbleRows.append("Ending balance as of " + str(unionDataFrame[DATE_COL].iloc[transactionCount-1]) +",," + npNum2Str(unionDataFrame[BAL_COL].iloc[transactionCount-1]) + "," +"\n")
    preAmbleRows.append(",,," +"\n")
    preAmbleRows.append(DATE_COL+","+DESC_COL+","+AMNT_COL+","+BAL_COL +"\n")
    preAmbleRows.append(str(unionDataFrame[DATE_COL].iloc[0])+","+"Beginning balance as of " + str(unionDataFrame[DATE_COL].iloc[0]) +",," + npNum2Str(unionDataFrame[BAL_COL].iloc[0]) +"\n")

    File_object = open(outFile,'w')
    File_object.writelines(preAmbleRows)
    for index, row in unionDataFrame.iterrows():
        rowString = str(row[DATE_COL]) + "," + stripCommas(row[DESC_COL]) + "," + npNum2Str(row[AMNT_COL])+ "," + npNum2Str(row[BAL_COL]) +"\n"
        File_object.write(rowString)

    File_object.close()
