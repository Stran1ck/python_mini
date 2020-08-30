import datetime as dt

y, m, d = map(int, input().split())
day = dt.date(y, m, d)
dayz = dt.timedelta(days=int(input()))
daydelta = day + dayz
print(daydelta.year, daydelta.month, daydelta.day)
