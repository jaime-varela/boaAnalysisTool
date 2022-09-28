
from globals.column_names import BOA_AMNT_COL
import matplotlib.pyplot as plt
import numpy as np

# TODO get this out of here
CLASS_COL = 'class'

def classification_pi_chart(classified_df,strip_deposits=True):
    new_df = classified_df[[BOA_AMNT_COL,CLASS_COL]].copy()
    if strip_deposits:
        new_df = new_df[new_df[BOA_AMNT_COL] < 0]
    labels = classified_df[CLASS_COL].unique()
    totals = new_df.groupby(CLASS_COL)[BOA_AMNT_COL].sum()
    values = []
    for label in labels:
        value = -totals[label]
        values.append(value)
    plt.pie(values, labels = labels)
    plt.show()

