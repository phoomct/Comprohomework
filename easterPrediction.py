""" easterPrediction """
def main():
    """ A formula for computing Easter in the years
    1900-2099 from the input(year) is as follows:
    a = year%19
    b = year%4
    c = year%7
    d = (19a+24)%30
    e = (2b+4c+6d+5)%7
    Easter predicted date = March 22 + d + e
    Except for 1954, 1981, 2049 and 2076 that the predicted date is one week too late.
    Write a program that inputs a year,
    verifies that the input year is in range and print out the date of Easter that year. """
    predicted = [1954, 1981, 2049, 2076]
    year = int(input())
    first = year % 19
    second = year % 4
    third = year % 7
    forth = ((19 * first) + 24) % 30
    fifth = ((2 * second) + (4 * third) + (6 * forth) + 5) % 7
    date = 22 + forth + fifth
    if year in predicted:
        date = date - 7
    if (year >= 1900) and (year <= 2099):
        if date > 31:
            print("April %d, %d"%(date - 31, year))
        else:
            print("March %d, %d"%(date, year))
    else:
        print("Invalid input.")
main()
