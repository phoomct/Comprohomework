""" Exponential Equation """
def main():
    """ y = 2 - x + 3/7 x2 - 5/11 x3 + log10(x) """
    import math
    num = float(input())
    ans = 2 - num + (3 / 7 * (num ** 2)) - (5 / 11 * (num ** 3)) + math.log10(num)
    print(ans)
main()
