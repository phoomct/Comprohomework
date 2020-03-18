""" Atbash cipher """
def main():
    """ The Atbash cipher is a very common, simple cipher. The Atbash Cipher simply reverses the
     plaintext alphabet to create theciphertext alphabet. That is,
      the first letter of the alphabet is encrypted to the last letter of the alphabet,
    the second letter to the penultimate letter and so forth as follow:
    Uppercase
    Plain text: ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Cipher text: ZYXWVUTSRQPONMLKJIHGFEDCBA
    Lowercase
    Plain text: abcdefghijklmnopqrstuvwxyz
    Cipher text: zyxwvutsrqponmlkjihgfedcba
    Numbers
    Plain text: 0123456789
    Cipher text: 9876543210
    Write a program that gets the input string from the user where the string can include uppercase,
    lowercase and numbers, then retuns the cipher text of the input. """
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    upper2 = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    lower2 = 'zyxwvutsrqponmlkjihgfedcba'
    num = '0123456789'
    num2 = '9876543210'
    data = input()
    for i in range(len(data)):
        if (data[i].isnumeric()) == True:
            num3 = num.find(data[i])
            print(num2[num3], end="")
        elif (data[i].isupper() == True) and (data[i].isalpha() == True):
            upper3 = upper.find(data[i])
            print(upper2[upper3], end="")
        elif (data[i].islower() == True) and (data[i].isalpha() == True):
            lower3 = lower.find(data[i])
            print(lower2[lower3], end="")
        else:
            print(data[i], end="")
main()
