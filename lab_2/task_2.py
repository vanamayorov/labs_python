# 2. Create a class called Rational for performing arithmetic with fractions. Write a program to test your class.
# Use integer variables to represent the private data of the class – the numerator and the denominator.
# Provide a init() method that enables an object of this class to be initialized when it’s declared.
# The init() should contain default parameter values in case no initializers are provided and should
# store the fraction in reduced form.
# For example, the fraction 2/4 would be stored in the object as 1 in the numerator and 2 in the denominator.
# Provide public methods that perform each of the following tasks:
# - printing Rational numbers in the form a/b, where a is the numerator and b is the denominator.
# - printing Rational numbers in floating-point format.
from math import gcd

"""Script with Rational class which performs arithmetic with fractions"""


class Rational:
    """Rational class with methods which perform arithmetic operations with fractions"""

    def __init__(self, numerator=0, denominator=1):
        if not isinstance(numerator, int):
            raise TypeError("The numerator must be an integer")

        if not isinstance(denominator, int):
            raise TypeError("The denominator must be an integer")

        if not denominator:
            raise ZeroDivisionError("The denominator can`t be zero")

        self.numerator = numerator // gcd(numerator, denominator)
        self.denominator = denominator // gcd(numerator, denominator)

    def print_fraction(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def print_float(self):
        return self.numerator / self.denominator

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.denominator * self.numerator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)


def main():
    first_fr = Rational(2, 1)
    print(f'fraction №1: {first_fr.print_float()}, {first_fr.print_fraction()}')

    second_fr = Rational(6, 3)
    print(f'fraction №2: {second_fr.print_float()}, {second_fr.print_fraction()}')

    new_fr = first_fr * second_fr
    print(f'fraction №3: {new_fr.print_float()}, {new_fr.print_fraction()}')

    try:
        false_fr = Rational(1, 0)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
