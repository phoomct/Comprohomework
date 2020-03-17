""" Banknote """
def main():
    """ In a BankBank land, there are 5 banknotes as $800, $200, $150, $60 and $10.
    Write a program that helps the BB Bank to count the number of each banknote
    from the total amount of value, where the bank will
    always try to return the biggest bank notes first."""
    money = int(input())
    print(money//800)
    money = money % 800
    print(money//200)
    money = money % 200
    print(money//150)
    money = money % 150
    print(money//60)
    money = money % 60
    print(money//10)
main()
