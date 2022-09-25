from textblob.classifiers import NaiveBayesClassifier
import pandas as pd
from globals.column_names import BAYES_TRAINING_CLASS_COL,BAYES_TRAINING_DESCRIPTION_COL, BOA_DESC_COL

def classify_using_naive_bayes(input_df,training_file=None):


    if training_file is None:
        print("error: provide valid training file")
        return
    training_df = pd.read_csv(training_file)
    training_tuples = []
    for ind, row in training_df.iterrows():
        des= row[BAYES_TRAINING_DESCRIPTION_COL]
        classification = row[BAYES_TRAINING_CLASS_COL]
        training_tuples.append((des,classification))
    # TODO: change this so that I don't create a classifier every time (create stateful classes or something)
    classifier = NaiveBayesClassifier(training_tuples)
    classifications = []
    classified_df = input_df
    for ind, row in input_df.iterrows():
        desc = row[BOA_DESC_COL]
        classification = classifier.classify(desc)
        classifications.append(classification)
    classified_df['class'] = classifications
    return classified_df