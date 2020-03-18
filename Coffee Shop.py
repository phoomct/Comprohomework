""" Coffee Shop """
def main():
    """The IT coffee shop sells 3 different types of coffess as follows:
    Robusta coffee 390 baht per kg, ***Promotion Free 2 kg of Robusta coffee,
    every 15 kg Robusta coffee order.
    Liberica coffee 380 baht per kg, ***Promotion Free 2 kg of Liberica coffee,
    every 15 kg Liberica coffee order.
    Arabica coffee 440 baht per kg, ***Promotion Free 1 kg of Arabica coffee,
    every 15 kg Arabica coffee order.
    For each transaction, customer need to pay 5% shipping cost.
    IF the total amount is more than 5,000 baht,
    the shipping cost is free.
    Write a program that calculate the cost of an order."""
    data = input()
    rob, lib, arab = data.split(',')
    rob, lib, arab = int(rob), int(lib), int(arab)
    if rob >= 17:
        rob = rob-((rob//15)*2)
    robc = 390 * rob
    if lib >= 17:
        lib = lib - ((lib // 15) * 2)
    libc = 380*lib
    if arab >= 16:
        arab = arab-(arab // 15)
    arabc = 440 * arab
    total = robc + libc + arabc
    ship = 5 * total / 100
    if total >= 5000:
        ship = 0
    print('Coffee cost: %.2f'%total)
    print('Shipping cost: %.2f'%ship)
main()
