""" Pizza price """
def main():
    """ Write a program that calculate the cost per square inch of circular pizza,
    given its diameter and price.
    The formula for area is A=πr2 """
    import math
    diamete = float(input())
    cost = float(input())
    radiance = diamete / 2
    area = math.pi * radiance ** 2
    price = cost/ area
    print(price)
main()
