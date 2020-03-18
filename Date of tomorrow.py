""" Date of tomorrow """
def main():
    """ Write a Python program to get next day of a given date (dd-mm-yyyy)
    *** Don't forget leap year where there are 366 days in that year,
    meaning there are 29 days in February
    A year is a leap year if it is divisible by 4, unless it is a century year that
    is not divisible by 400.
    (e.g., 1800 and 1900 are not leap years while 1600 and 2000 are.)"""
    date = input()
    day, month, year = date.split("-")
    day, month, year = int(day), int(month), int(year)
    if year % 400 == 0 or year % 4 == 0 and year %100 != 0:
        leap_year = True
    else:
        leap_year = False
    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        if leap_year == True:
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30
    if day < month_length:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    print("%02d-%02d-%04d" %(day, month, year))
main()
