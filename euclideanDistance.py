""" euclideanDistance """
def main():
    """ Write a program that gets 4 numbers from the user as
    q1, q2, p1, p2 where Q is a point in 2-dimentional plane at position (q1, q2) and
    point P is at (p1, p2). Find the Euclidean distance between Q and P where the Euclidean d
    istance between any 2 points Q and P is """
    import math
    voq1 = float(input())
    voq2 = float(input())
    vop1 = float(input())
    vop2 = float(input())
    distance = math.sqrt(((voq1 - vop1) ** 2) + ((voq2 - vop2) ** 2))
    print(distance)
main()
