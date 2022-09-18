

# FIXME FIXME FIXME code duplication
DATE_COL = 'Date'
DESC_COL = 'Description'
AMNT_COL = 'Amount'
BAL_COL = 'Running Bal.'

SUMMARY_CONST = 'Summary Amt.'

# (expected_class: {acceptable_synonyms})  dictionary
INTERNAL_CLASS_DICT = {
    'entertainment': {"netflix","hbo","appletv","hulu","loews","amc", "disneyplus"},
    'transportation': {"lyft", "uber trip", "mbta", "bluebike"},
    'dining' : {"uber eats", "grubhub", "doordash", "sweetgreen","caffe", "dunkin", "starbucks"},
    'goods' : {"amazon","amzn","target","cvs", "walgreens", "star market"},
    'bills' : {"geico", "eversource","allstate"},
    'investments' : {"betterment","wealthfront"},
    'cash' : {'BKOFAMERICA','venmo', " atm "}
}

def dictionary_based_char_match(description,dict=INTERNAL_CLASS_DICT):
    description = description.lower()
    for (classification, keywords) in dict.items():
        if any([keyword.lower() in description for keyword in keywords]):
            return classification
    return "unknown"



def classify_statement_from_rule_set(stmt_df, classification_function=dictionary_based_char_match):
    classified_df = stmt_df
    classifications = []
    for desc in stmt_df[DESC_COL].values:
        classifications.append(classification_function(desc))
    classified_df['classes'] = classifications
    return classified_df