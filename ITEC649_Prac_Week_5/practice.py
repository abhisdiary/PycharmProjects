"""
Practice problems for Python in COMP249/ITEC649

Author: Steve Cassidy
Email: steve.cassidy@mq.edu.au
"""


def longest(string1, string2):
    """Return the longest string from the two arguments,
    if the strings are the same length, return the first string

    >>> longest('this', 'that one')
    'that one'

    >>> longest('this one', 'that')
    'this one'

    >>> longest('this', 'that')
    'this'

    ## Test that the function returns a value (rather than printing)
    >>> longest('this', 'that one') is 'that one'
    True
    """
    # your code here
    if len(string1) == len(string2):
        return string1
    elif len(string1) > len(string2):
        return string1
    else:
        return string2


def count_over(thelist, n):
    """Return the number of integers in thelist that are
    greater than the integer n

    >>> count_over([1,2,4,5,6], 3)
    3
    >>> count_over([5,1,3,5,1], 3)
    2
    >>> count_over([0,0,0,0,0], 3)
    0
    >>> count_over([1,2,4,5,6], 3) == 3
    True
    """
    # your code here
    c = 0
    for i in thelist:
        if i > n:
            c = c + 1
    return c


def extract_product(pairs):
    """Given a list of pairs of integers, return a list with the product of elements from each pair
    (that is, the numbers multiplied together)

    If an item is not a pair, return None for that element

    >>> extract_product([(2,3),(1,4)])
    [6, 4]
    >>> extract_product([(2,3),(1,4),(2, 9)])
    [6, 4, 18]
    >>> extract_product([(0,5),(3,6,7)])
    [0, None]
    >>> extract_product([(1,3),(3,4)]) ==  [3, 12]
    True
    """
    # your code here
    myList = []
    for i in pairs:
        if len(i) > 2:
            myList.append(None)
        else:
            myList.append(i[0] * i[1])
    return myList


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
