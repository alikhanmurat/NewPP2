import datetime

def date_diff(date1, date2):
    delta = date2 - date1
    return delta.total_seconds()

date1 = datetime.datetime(2023, 3, 5, 10, 30, 0)
date2 = datetime.datetime.now()

print (date_diff(date1, date2))
