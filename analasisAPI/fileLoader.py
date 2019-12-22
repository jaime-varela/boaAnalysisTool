import pandas as pd



DATE_COL = 'Date'
DESC_COL = 'Description'
AMNT_COL = 'Amount'
BAL_COL = 'Running Bal.'

# the current BOA file has six useless rows so we do not read those
# TODO: make this more robust for different bank formats
def LoadFile(filePath):
    '''
        Input:
            filepath -> path to BOA csv file
        Output: 
            pandas dataframe
    '''
    dtypes = {'A':'str','B':'str','C':'float','D':'float'}
    parse_dates = [0]
    return pd.read_csv(filePath,skiprows=[0,1,2,3,4,5,7],dtype=dtypes,parse_dates=parse_dates)