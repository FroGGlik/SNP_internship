import datetime

def date_in_future(days: int):
    if isinstance(days, int):
        return datetime.datetime.now() + datetime.timedelta(days=days)
    else:
        return datetime.datetime.now()


print(date_in_future([]))
print(date_in_future(2))