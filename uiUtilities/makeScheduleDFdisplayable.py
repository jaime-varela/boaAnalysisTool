from .dropdownData import dayOfWeekToLetter, stringToEnumGrouping
from .dropdownData import stringToEnumTextProcess, dayOfWeekToName
from .dropdownData import dayOfWeekToLetter, EnumScheduleToString
import numpy as np

#FIXME: get rid of this copied var (this is a problem!)
SCHEDULE_COLUMNS = ['Description','Frequency','Avg. Cost','Schedule']

def scheduleToString(x):
    if not isinstance(x,np.ndarray):
        if x < 0:
            v = -1 * x
            return str(v)
        else:
            return dayOfWeekToName[x]
    # daily handler
    x.sort()
    retStr = ""
    for index in range(len(x)):
        retStr += dayOfWeekToLetter[x[index]]
        if index != len(x) -1:
            retStr += ","
    return retStr

def makeScheduleDFdisplayable(scheduledDF):
    description = SCHEDULE_COLUMNS[0]
    frequency = SCHEDULE_COLUMNS[1]
    avgCost = SCHEDULE_COLUMNS[2]
    sched = SCHEDULE_COLUMNS[3]
    newDF = scheduledDF
    newDF[frequency] = newDF[frequency].apply(lambda x: EnumScheduleToString[x])
    newDF[avgCost] = newDF[avgCost].apply(lambda x: str( np.round(x,decimals = 2) ) )
    newDF[sched] = newDF[sched].apply(lambda x: scheduleToString(x))
    return newDF




