"""
This program will calculate the Hypotenuse using the Pythagorean Theorem
The Pythagorean Theorem describes the relationship between the sides of a right triangle.
It states that for any right triangle with sides of length a and b, and hypotenuse of length c, a2 + b2 = c2
"""


def main():
    sidea = int(input('Input the side "a" of the right triangle: '))
    sideb = int(input('Input the side "b" of the right triangle: '))
    hypotenuse = ((sidea**2) + (sideb**2))
    print('The value of the Hypotenuse is: ' + str(hypotenuse))


if __name__ == '__main__':
    main()
