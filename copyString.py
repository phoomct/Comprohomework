""" Copy String """
def main():
    """ Write a Python function to get a string made of 4 copies
    of the last two characters of a specified string."""
    print((((input())[::-1])[0:2])[::-1] * 4)
main()
