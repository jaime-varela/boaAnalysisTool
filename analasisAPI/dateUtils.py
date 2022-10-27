
from enum import Enum, IntEnum
import numpy as np
import datetime

class WeekDay(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDENESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def day_array_for_weekly_schedule(start_date,end_date,dayOfWeek_enum):
    '''
        Returns a binary_mask = [0,0,1,0, ...] where the binary_mask[day_index] = 1 
        if the index is on the day of the week scheduled.  day_index = 0 corresponds to the start day
    '''
    assert start_date < end_date ,"End date must be after start date."
    first_week_day = start_date.today().weekday()

    delta = end_date - start_date
    num_days = delta.days + 1 # must include the original day
    result = np.zeros(num_days,dtype=np.int8)
    for ind in range(result.shape[0]):
        if (ind - (int(dayOfWeek_enum) - first_week_day) ) % 7 == 0:
            result[ind] = 1
    return result