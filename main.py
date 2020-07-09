# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function

import random


def generateList():
    randomlist = []
    for i in range(0, 15):
        n = random.randint(1, 30)
        randomlist.append(n)

    return randomlist


def main():
    list = generateList()
    newLis = [list[0], list[-1]]
    print(list)
    print(newLis)


main()
