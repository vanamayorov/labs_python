# 1. Modify the class Rational of Lab No2 to perform the following tasks:
# - adding two Rational numbers. The result should be stored in reduced form;
# - subtracting two Rational numbers. The result should be stored in reduced form;
# - multiplying two Rational numbers. The result should be stored in reduced form;
# - dividing two Rational numbers. The result should be stored in reduced form;
# - comparison two Rational numbers.

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
        if self.get_type(other) == 'rational':
            numerator = self.numerator * other.denominator + other.denominator * self.numerator
            denominator = self.denominator * other.denominator
            return Rational(numerator, denominator)
        else:
            numerator = self.numerator + self.denominator * other
            denominator = self.denominator
            return Rational(numerator, denominator)

    def __iadd__(self, other):
        if self.get_type(other) == 'rational':
            self.numerator = self.numerator * other.denominator + other.denominator * self.numerator
            self.denominator = self.denominator * other.denominator
            return self
        else:
            self.numerator = self.numerator + self.denominator * other
            return self

    def __sub__(self, other):
        if self.get_type(other) == 'rational':
            numerator = self.numerator * other.denominator - other.numerator * self.denominator
            denominator = self.denominator * other.denominator
            return Rational(numerator, denominator)
        else:
            numerator = self.numerator - self.denominator * other
            denominator = self.denominator
            return Rational(numerator, denominator)

    def __isub__(self, other):
        if self.get_type(other) == 'rational':
            self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
            self.denominator = self.denominator * other.denominator
            return self
        else:
            self.numerator = self.numerator - self.denominator * other
            return self

    def __mul__(self, other):
        if self.get_type(other) == 'rational':
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            return Rational(numerator, denominator)
        else:
            numerator = self.numerator * other
            denominator = self.denominator
            return Rational(numerator, denominator)

    def __imul__(self, other):
        if self.get_type(other) == 'rational':
            self.numerator = self.numerator * other.numerator
            self.denominator = self.denominator * other.denominator
            return self
        else:
            self.numerator = self.numerator * other
            return self

    def __floordiv__(self, other):
        if self.get_type(other) == 'rational':
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.denominator
            return Rational(numerator, denominator)
        else:
            numerator = self.numerator
            denominator = self.denominator * other
            return Rational(numerator, denominator)

    def __ifloordiv__(self, other):
        if self.get_type(other) == 'rational':
            self.numerator = self.numerator * other.denominator
            self.denominator = self.denominator * other.denominator
            return self
        else:
            self.denominator = self.denominator * other
            return self

    def __eq__(self, other):
        first_num = self.numerator * other.denominator
        second_num = self.denominator * other.numerator
        return first_num == second_num

    @staticmethod
    def get_type(obj):
        if not isinstance(obj, int) and not isinstance(obj, Rational):
            raise TypeError('Number must be either int, Rational type')
        if isinstance(obj, int):
            return 'int'
        else:
            return 'rational'


def main():
    first_fr = Rational(3, 4)
    print(f'fraction №1: {first_fr.print_float()}, {first_fr.print_fraction()}')

    second_fr = Rational(6, 4)
    print(f'fraction №2: {second_fr.print_float()}, {second_fr.print_fraction()}')

    new_fr = first_fr * second_fr
    print(f'fraction №3: {new_fr.print_float()}, {new_fr.print_fraction()}')

    first_fr += 1
    print(f'{first_fr.print_float()}, {first_fr.print_fraction()}')
    print(first_fr == second_fr)
    first_fr += second_fr
    print(f'{first_fr.print_float()}, {first_fr.print_fraction()}')


if __name__ == '__main__':
    main()
