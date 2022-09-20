import pandas as pd
from globals.column_names import BOA_SUMMARY_CONST,BOA_AMNT_COL,BOA_BAL_COL,BOA_DATE_COL,BOA_DESC_COL

def isChaseFile(in_filename):
    return False
def LoadChaseFile(in_filename):
    assert "not implemented"
    return



def isChaseFile(in_filename):
    return False

def LoadChaseFile(in_filename):
    assert "not implemented"
    return


# Misc utils
def stripCommas(inputStr):
    return inputStr.replace(",","")


# BOA utils----------------
def isBoaFile(in_filename):
    # TODO: not multi-national
    with open(in_filename) as myfile:
        head = [next(myfile) for x in range(6)] # first six line
    firstLineCondition = head[0].split(",")[0] == "Description"
    thirdLineCondition = head[2].split(",")[0] == "Total credits"
    fourthLineCondition= head[3].split(",")[0] == "Total debits"
    return firstLineCondition and thirdLineCondition and fourthLineCondition

def LoadBoaFile(in_filename):
    parse_dates = [0]
    dataFrame = pd.read_csv(in_filename,skiprows=[0,1,2,3,4,5,7],parse_dates=parse_dates)
    dataFrame[BOA_DESC_COL] = dataFrame[BOA_DESC_COL].apply(lambda x: stripCommas(x))
    dataFrame[BOA_AMNT_COL] = dataFrame[BOA_AMNT_COL].apply(lambda x: stripCommas(x))
    dataFrame[BOA_BAL_COL] = dataFrame[BOA_BAL_COL].apply(lambda x: stripCommas(x))
    dataFrame[BOA_AMNT_COL] = dataFrame[BOA_AMNT_COL].astype('float')
    dataFrame[BOA_BAL_COL] = dataFrame[BOA_BAL_COL].astype('float')    
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
    unionDataFrame.sort_values(by=[BOA_DATE_COL])
    transactionCount = unionDataFrame[BOA_DATE_COL].count()
    preAmbleRows = []
    preAmbleRows.append(BOA_DESC_COL+',,'+BOA_SUMMARY_CONST+"," +"\n")
    preAmbleRows.append("Beginning balance as of " + str(unionDataFrame[BOA_DATE_COL].iloc[0]) +",," + npNum2Str(unionDataFrame[BOA_BAL_COL].iloc[0]) + "," +"\n")
    preAmbleRows.append(",,," +"\n")
    preAmbleRows.append(",,," +"\n")
    preAmbleRows.append("Ending balance as of " + str(unionDataFrame[BOA_DATE_COL].iloc[transactionCount-1]) +",," + npNum2Str(unionDataFrame[BOA_BAL_COL].iloc[transactionCount-1]) + "," +"\n")
    preAmbleRows.append(",,," +"\n")
    preAmbleRows.append(BOA_DATE_COL+","+BOA_DESC_COL+","+BOA_AMNT_COL+","+BOA_BAL_COL +"\n")
    preAmbleRows.append(str(unionDataFrame[BOA_DATE_COL].iloc[0])+","+"Beginning balance as of " + str(unionDataFrame[BOA_DATE_COL].iloc[0]) +",," + npNum2Str(unionDataFrame[BOA_BAL_COL].iloc[0]) +"\n")

    File_object = open(outFile,'w')
    File_object.writelines(preAmbleRows)
    for index, row in unionDataFrame.iterrows():
        rowString = str(row[BOA_DATE_COL]) + "," + stripCommas(row[BOA_DESC_COL]) + "," + npNum2Str(row[BOA_AMNT_COL])+ "," + npNum2Str(row[BOA_BAL_COL]) +"\n"
        File_object.write(rowString)

    File_object.close()
def isBoaCreditFile(in_filename):
    return False

def LoadBoaCreditFile(in_filename):
    assert "not implemented"
    return
