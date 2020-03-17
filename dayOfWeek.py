""" dayOfWeek """
def main():
    """ dayOfWeek """
    import datetime
    date = input()
    day, month, year = date.split(":")
    day, month, year = int(day), int(month), int(year)
    dayofweek = datetime.date(year, month, day).strftime("%A")
    print(dayofweek)
main()
