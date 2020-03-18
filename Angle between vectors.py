""" Angle between vectors """
def main():
    """Write a program to find the angle (θ) in degree between
    vector A = (a1, a2) and B = (b1, b2) """
    import math as m
    vecter_a = input()
    vecter_b = input()
    va1, va2 = vecter_a.split(",")
    vb1, vb2 = vecter_b.split(",")
    va1, va2, vb1, vb2 = float(va1), float(va2), float(vb1), float(vb2)
    angle = va1 * vb1 + va2 * vb2
    angle_2 = m.sqrt((va1 ** 2) + (va2 ** 2))
    angle_2f = m.sqrt(((vb1 ** 2) + (vb2 ** 2)))
    final = angle_2 * angle_2f
    angle = angle / final
    degree = m.degrees(m.acos(angle))
    print("%.2f" %degree)
main()
