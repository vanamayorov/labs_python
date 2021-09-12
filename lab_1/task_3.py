# Task 3
# Write a Python-script that determines whether the input string is the
# correct entry for the 'formula' according EBNF syntax (without
# using regular expressions).
#
# Formula = Number | (Formula Sign Formula)
# Sign = '+' | '-'
# Number = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
# Input: string
# Result: (True / False, The result value / None)
# Example,
# user_input = '1+2+4-2+5-1' result = (True, 9)
# user_input = '123' result = (True, 123)
# user_input = 'hello+12' result = (False, None)
# user_input = '2++12--3' result = (False, None)
# user_input = '' result = (False, None)

"""Task 3
    The Python-script checks if the input string is the correct formula
    according to EBNF syntax

    Not finished yet
"""

import argparse


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('expression', help='Math expression', type=str)
    args = parser.parse_args()

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    signs = ['+', '-']
    indicator = True
    string_output = ''

    if len(args.expression) != 0:
        if indicator:
            for char in args.expression:
                if char in numbers or char in signs:
                    string_output += char
                else:
                    string_output = None
                    indicator = False
                    break

        if indicator:
            for index, ch in enumerate(string_output):
                if index + 1 < len(string_output):
                    if ch in signs and string_output[
                        index + 1] in signs:
                        string_output = None
                        indicator = False
                        break

        if indicator:
            print(f'result = ({indicator}, {eval(string_output)})')
        else:
            print(f'result = ({indicator}, None)')
    else:
        print(f'result = (False, None)')


if __name__ == '__main__':
    main()
