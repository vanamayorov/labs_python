# Task 1
# Write a Python-script that performs simple arithmetic operations:
# '+', '-', '*', '/'. The type of operator and data are set on the
# command line when the script is run.The script should be
# launched like this:
# >>python my_task.py 1 * 2

"""Task 1
    This script takes 3 arguments, two of which are digits and
    the third is operator, from the command line and calculates the
    result using eval function.
"""

import argparse
import ast


def main():
    # parse arguments
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('firstNum', metavar='First num', help='first number')
    parser.add_argument('op', metavar='Operator', help='arithmetic operator')
    parser.add_argument('secondNum', metavar='Second num', help='second number')

    args = parser.parse_args()
    # calculates result using eval function
    try:
        if args.op not in ["+", "-", "/", "*"]:
            raise Exception("choose from '+', '-', '/', '*'")
        result = eval(args.firstNum + args.op + args.secondNum)
        print(result)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
