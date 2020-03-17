""" Flat rate """
def main():
    """ Students have multiple options of communication from their
    dormitory to the department such as motorcycle taxi,
    taxi, bus or bicycle, etc. However, most of these options are not practic
    al for rainy season. Thus,
     some students plan to buy their own car!
       There are 2 ways to buy a car:
    Pay cash: pay the total amount of money one time.
    Installment plan: pay some amount of money first,
    and then pay the rest monthly with some interest. Where
    Principle amount = Total amount - down payment
    The total interest = Principle amount x Annual
    interest rate x Total time (years)
    Monthly installment: (Principle amount + total interest) / (years*12)
    Let define: annual interest rate for 2019 = 3.25 (%)"""
    car = int(input())
    down = int(input())
    years = int(input())
    prin = car - down
    inter = float(prin * ((3.25 / 100) * years))
    install = (prin + inter)/(years * 12)
    print(int(inter))
    print(int(install))
main()
