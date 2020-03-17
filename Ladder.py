""" Ladder """
def main():
    """ Write a program to determine the length of a ladder required to reach a
     given height when leaned against a house.
    The height and the angle (in degree) of the ladder are given as input.
   length=  height/sin(angle (in radian)) """ 
    import math
    print(float(input())/math.sin(math.radians(float(input()))))
main()