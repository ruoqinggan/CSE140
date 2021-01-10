#!/usr/bin/env python3

"""
Based off of: http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

To run this script, type:

  python3 buyLotsOfFruit.py

Once you have correctly implemented the buyLotsOfFruit function,
the script should produce the output:

Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
"""

FRUIT_PRICES = {
    'apples': 2.00,
    'oranges': 1.50,
    'pears': 1.75,
    'limes': 0.75,
    'strawberries': 1.00
}

"""
orderList: List of (fruit, weight) tuples

Returns cost of order
"""


def buyLotsOfFruit(orderList):
    # initialized variable to hold total cost
    cost = 0

    # iterative through the list
    for x in orderList:
        # if the first elem in each tuple exists in dictionary
        if x[0] in FRUIT_PRICES:
            # calculates the cost using the price from dict
            cost += x[1] * FRUIT_PRICES[x[0]]
        # item doesn't exist in dict, prints out error msg and returns none
        else:
            print("There's an error in your order.")
            return None
    # returns total cost
    return cost


def main():
    orderList = [
        ('apples', 2.0),
        ('pears', 3.0),
        ('limes', 4.0)
    ]

    print("Cost of %s is %s." % (orderList, buyLotsOfFruit(orderList)))


if __name__ == '__main__':
    main()
