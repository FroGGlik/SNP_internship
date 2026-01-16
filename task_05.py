import datetime

def date_in_future(days):
    now = datetime.datetime.now()
    if isinstance(days, int):
        future_date = now + datetime.timedelta(days=days)
    else:
        future_date = now

    return future_date.strftime('%d-%m-%Y %H:%M:%S')


print(date_in_future([]))
print(date_in_future(2))