# Task 4
# You are given n bars of gold with weights: w1, w2, ..., wn and bag
# with capacity W.
# There is only one instance of each bar and for each bar you can either
# take it or not (hence you cannot take a fraction of a bar).
# Write a function that returns the maximum weight of gold that fits
# into a knapsack's capacity.
# The first parameter contains 'capacity' - integer describing the
# capacity of a knapsack.
# The next parameter contains 'weights' - list of weights of
# each gold bar.
# Output : Maximum weight of gold that fits into a knapsack
# with capacity of W.

"""Task 4
    The script takes arguments(bag capacity, list of gold weights) from the command line
    and calculates the maximum weight of gold that fits into a knapsack with the given capacity.
"""
import argparse
import ast


# Function makes a memorization table(matrix) with all combinations of gold weights
# and returns the most appropriate one.
def get_max_weight(items, capacity):

    n = len(items)

    # the declaration and assignment of a memorization table(matrix)
    V = [[0 for a in range(capacity + 1)] for i in range(n + 1)]

    # loop which fill the memorization table
    for i in range(n + 1):
        for a in range(capacity + 1):
            if i == 0 or a == 0:
                V[i][a] = 0
            elif items[i - 1] <= a:
                V[i][a] = max(items[i - 1] + V[i - 1][a - items[i - 1]], V[i - 1][a])
            else:
                V[i][a] = V[i - 1][a]

    return V[n][capacity]


def main():
    # parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("capacity", help="Capacity of a bag", type=int)
    parser.add_argument("weights", help="List of available weights", nargs='*')
    args = parser.parse_args()

    max_weight = get_max_weight([ast.literal_eval(weight) for weight in args.weights], args.capacity)

    print(f"Maximum weight that fits into a knapsack is {max_weight} with capacity of {args.capacity}")


if __name__ == "__main__":
    main()
