""" Leap year """
def main():
    """ A year is a leap year if it is divisible by 4, unless it is
    a century year that is not divisible by 400.
    (e.g., 1800 and 1900 are not leap years while 1600 and 2000 are.)
    Write a program that calculates whether a year is a leap year. """
    year = int(input())
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print("%d is a leap year."%year)
    else:
        print("%d is not a leap year."%year)
main()
