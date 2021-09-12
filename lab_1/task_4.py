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

"""
    NOT FINISHED YET
"""

# items = {
#     "f": 1,
#     "s": 2,
#     "t": 9
# }
#
#
# def get_weight(items):
#     weight = [items[item] for item in items]
#     return weight
#
#
# def make_memtable(items, A):
#     weight = get_weight(items)
#     n = len(weight)
#
#     V = [[0 for a in range(A + 1)] for i in range(n + 1)]
#
#     for i in range(n + 1):
#         for a in range(A + 1):
#             if i == 0 or a == 0:
#                 V[i][a] = 0
#             elif weight[i - 1] <= a:
#                 V[i][a] = max(weight[i - 1] + V[i - 1][a - weight[
#                     i - 1]], V[i - 1][a])
#             else:
#                 V[i][a] = V[i - 1][a]
#
#     return V, weight
#
#
# def get_selected_items(items, A):
#     V, weight = make_memtable(items, A)
#     n = len(weight)
#     res = V[n][A]
#     a = A
#     items_list = []
#
#     for i in range(n, 0, -1):
#         if res <= 0:
#             break
#         elif res == V[i - 1][a]:
#             continue
#         else:
#             items_list.append(weight[i - 1])
#             a -= weight[i - 1]
#             res -= weight[i - 1]
#
#     selected_stuff = []
#
#     for search in items_list:
#         for key, weight in items.items():
#             if weight == search:
#                 selected_stuff.append(key)
#     return selected_stuff
#
#
# stuff = get_selected_items(items, 5)
# totweight = sum([items[item] for item in stuff])
# print(stuff, totweight)

from collections import namedtuple

Item = namedtuple('Item', 'value weight')
items = Item(4, 15), Item(3, 4),
capacity = 20  # max weight we can put into the knapsack


def best_value(nitems, weight_limit):
    if nitems == 0:  # no items
        return 0  # zero value
    elif items[nitems - 1].weight > weight_limit:
        # new item is heavier than the current weight limit
        return best_value(nitems - 1,
                          weight_limit)  # don't include new item
    else:
        return max(  # max of with and without the new item
            best_value(nitems - 1, weight_limit),  # without
            best_value(nitems - 1,
                       weight_limit - items[nitems - 1].weight)
            + items[nitems - 1].value)  # with the new item


result = []
weight_limit = capacity
for i in reversed(range(len(items))):
    if best_value(i + 1, weight_limit) > best_value(i, weight_limit):
        # better with the i-th item
        result.append(items[i])  # include it in the result
        weight_limit -= items[i].weight


print(result)
