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
    according to EBNF syntax using loops and conditions.
"""

import argparse


def main():
    # parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('expression', help='Math expression', type=str)
    args = parser.parse_args()

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    signs = ['+', '-']
    indicator = True
    string_output = ''

    # condition checks whether there are any elements in the string
    if args.expression:
        for index, char in enumerate(args.expression):
            # condition checks scenarios when formula isn`t correct according to EBNF syntax
            if index + 1 <= len(args.expression) and not args.expression[0] in signs \
                    and not args.expression[len(args.expression) - 1] in signs:
                if char in numbers or (char in signs and not args.expression[index + 1] in signs):
                    string_output += char
                else:
                    string_output = None
                    indicator = False
                    break
            else:
                indicator = False
        # condition to print the result
        if indicator:
            print(f'result = ({indicator}, {eval(string_output)})')
        else:
            print(f'result = ({indicator}, None)')
    else:
        indicator = False
        print(f'result = ({indicator}, None)')


if __name__ == '__main__':
    main()
