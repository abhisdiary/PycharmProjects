"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

    Randomly generate two lists to test this
    Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def common_elements(list_1, list_2):
    new_list = list(set(list_1) & set(list_2))
    return new_list


def list_generator(list_length, min_val, max_val):
    a_list = []
    i = 0
    while i < list_length:
        a_list.append(random.randrange(min_val, max_val))
        i += 1
    print(a_list)
    return a_list


print(common_elements(a, b))
print(common_elements(list_generator(10, 1, 100), list_generator(15, 1, 100)))
