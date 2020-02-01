from analasisAPI.subscriptionFinder import textProcessing, groupingAlgorithm,scheduleTypeEnum



stringToEnumGrouping = {
   'First char match' : groupingAlgorithm.FirstNdigits,
   'Last char match' : groupingAlgorithm.LastNdigits,
   'String similarity'  : groupingAlgorithm.StringSimilarity,
   'First+Last char match' : groupingAlgorithm.FirstNandLastMdigits
}

stringToEnumTextProcess = {
    'Numeric removal' : textProcessing.NumericRemoval,
    'Non-alphabet removal' : textProcessing.NonAlphabetCharRemoval,
    'Non-alphanumeric removal' : textProcessing.NonAlphaNumericCharRemoval
}

dayOfWeekToName = {
    0 : 'Monday',
    1 : 'Tuesday',
    2 : 'Wedenesday',
    3 : 'Thursday',
    4 : 'Friday',
    5 : 'Saturday',
    6 : 'Sunday'
}

dayOfWeekToLetter = {
    0 : 'M',
    1 : 'T',
    2 : 'W',
    3 : 'Th',
    4 : 'F',
    5 : 'S',
    6 : 'Su'
}


EnumScheduleToString = {
    scheduleTypeEnum.Daily : 'Daily',
    scheduleTypeEnum.Weekly : 'Weekly',
    scheduleTypeEnum.Monthly : 'Monthly',
    scheduleTypeEnum.NoSchedule : ''
}


settingsDefault = {
    'firstNchar' : 6,
    'lastNchar' : 4,
    'similarityMeasure' : 80.0 
}