""" Cell Phone Bill """
def main():
    """ A particular cell phone plan includes 50 minutes of air time and 50 text messages
     for $15.00 a month.Each additional minute of air time costs $0.25,while additional text message
     cost $0.15 each.All cell phone billsinclude an additional charge of $0.44 to s
     upport 911 call centers,
       and the entire bill (including the 911 charge)
    is subject to 5 percent sales tax.
    Write a program that reads the number o
    f minutes and text messages used in a month from the user.
    Display the base charge, additional minutes charge (if any),
    additional text message charge (if any), the 911 fee, tax and total bill amount.
    Only display the additional minute and text message charges if the user incurred costs
    in these categories. Ensure that
    all of the charges are displayed using 2 decimal places. """
    addair = 0.25
    addtext = 0.15
    cop = 0.44
    bill = input()
    air, text = bill.split(",")
    air, text = int(air), int(text)
    print("Cell phone plan: $15.00")
    if air > 50 and text <= 50:
        airs = air - 50
        airs = airs * addair
        total = 15 + airs + cop
        tax = total * 0.05
        total = total + tax
        print("Additional air time: $%.2f" %airs)
    elif air > 50 and text > 50:
        airs = air - 50
        airs = airs * addair
        textt = text - 50
        textt = textt * addtext
        total = 15 + airs + textt + cop
        tax = total * 0.05
        total = total + tax
        print("Additional air time: $%.2f" %airs)
        print(("Additional text messages: $%.2f" %textt))
    elif air <= 50 and text > 50:
        text = text - 50
        tex = text * addtext
        total = 15 + tex + cop
        tax = total * 0.05
        total = total + tax
        print(("Additional text messages: $%.2f" %tex))
    else:
        total = 15 + 0.44
        tax = total * 0.05
        total = total + tax
    print("911 Call center support: $0.44")
    print("Total: $%.2f"%total)
main()
