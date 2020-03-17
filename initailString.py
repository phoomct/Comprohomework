""" initail String """
def main():
    """ Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.  """
    data = input()
    st1 = data[0:2]
    data = data[::-1]
    st2 = data[0:2]
    st2 = st2[::-1]
    print(st1+st2)
main()