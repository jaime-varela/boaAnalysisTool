
from globals.column_names import DESC_COL

# (expected_class: {acceptable_synonyms})  dictionary
INTERNAL_CLASS_DICT = {
    'entertainment': {"netflix","hbo","appletv","hulu","loews","amc", "disneyplus"},
    'transportation': {"lyft", "uber trip", "mbta", "bluebike"},
    'dining' : {"uber eats", "grubhub", "doordash", "sweetgreen","caffe", "dunkin", "starbucks"},
    'goods' : {"amazon","amzn","target","cvs", "walgreens", "star market", "walmart", "bedbath", "containerstore", "HOME DEPOT", "shaws"},
    'bills' : {"geico", "eversource","allstate", "national grid", "comcast"},
    'investments' : {"betterment","wealthfront"},
    'cash' : {'BKOFAMERICA','venmo', " atm "},
    'housing': {'jay zola', 'Collingham','check ', 'Micozzi'},
    'fitness': {'everybodyfights'}
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
    classified_df['class'] = classifications
    return classified_df
