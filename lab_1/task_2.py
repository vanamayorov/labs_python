# Task 2
# Write a Python-script that performs the standard math functions
# on the data. The name of function and data are set on the command
# line when the script is run. The script should be launched like this:
# >>python my_task.py add 1 2

"""Task 2
    The Python-script safely runs Python functions from command line.
"""
import argparse
import ast
import numpy as np


def main():
    # parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("function", help="Python function to run.")
    parser.add_argument("args", nargs='*')
    opt = parser.parse_args()

    # find a function from the numpy module
    func = getattr(np, opt.function)
    # literal_eval func casts string elements of list into integers
    args = [ast.literal_eval(arg) for arg in opt.args]

    # runs the function and passes in the args, print the output to console
    np.seterr(all="raise")
    try:
        result = func(*args)
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
