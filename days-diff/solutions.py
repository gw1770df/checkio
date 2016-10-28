h366 = lambda year : (not year % 4 and not year % 100 and not year % 400) or (not year % 4 and year % 100)
h29  = lambda year : 29 if h366(year) else 28
month_day = (0, 31, h29,31,30,31,30,31,31,30,31,30,31)
​
def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    if date1[0] > date2[0]:
        date1, date2 = date2, date1
    days = sum(map(lambda x: 366 if h366(x) else 365, range(date1[0], date2[0])))
    return abs(days - get_days(*date1) + get_days(*date2))
​
def get_days(y, m, d):
    return sum([month_day[i](y) if callable(month_day[i]) else month_day[i] for i in range(1, m)]) + d - 1
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print days_diff((1, 1, 1), (9999, 1, 1))
