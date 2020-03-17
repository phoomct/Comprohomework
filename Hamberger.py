""" Hamberger """
def main():
    """  The burger restuarant in your neighbourhood got a new scrolling LED sign.
    They want to advertise thier new meat lover burger where there is only bun and meat!
    They create a hamberger string as |
    (a vertical bar) stands for a bun and * stands for a slide of meat where
    one bun can hold only 2 pieces of meat.
    For example, ||**********||| is a hamburger
    (but on the horizontal view).
    where || stands for 2 pieces of bun (on the left)
    and ||| stands for 3 pieces of bun (on the right).
    ********** is ten slides of meat. (No vegetable).
    Given numbers of bread on the left and right, print a string of hamburger. """
    bread_top = (int(input()))
    bread_topp = bread_top *'|'
    bread_bottom = int(input())
    bread_bottomm = bread_bottom * '|'
    middle = ((bread_bottom + bread_top) * 2) * '*'
    ham = bread_topp + middle + bread_bottomm
    print(ham)
main()
