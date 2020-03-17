""" Number Palindrome """
def main():
    """ A palindrome is a word, number, phrase, or other sequence of characters which reads the same 
    backward as forward, such as madam or racecar or the number 10801. Write a program that get an input number, n,
     from the user and return the number of palindrom numbers from 1 to n. For example, If user input (n) = 20,
     then the output will be 10 since there are 10 numbers from 1-20 that are palindrome 
     (including 1, 2, 3, 4, 5, 6, 7, 8, 9, 11). """
    data = input()
    data = int(data)
    count = 0
    for i in range(data):
        i = i + 1
        iii = str(i)
        uuu = str(i)[::-1]
        if uuu == iii:
            count = count + 1
    print(count)
main()