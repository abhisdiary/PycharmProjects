def boolean_operators():
    print("========== Boolean Operations ==========")
    print(True and True)  # True
    print(True or False)  # True
    print(not True)  # False
    print(not False and not True or False)  # False
    print(7 > 6 >= 6)  # True
    print(3 != 3 or 4 == 4)  # True
    print(not 5 > 2)  # False
    print(not 5 < 3 and True or 6 <= 6 and not False)  # True


def dictionary_operations():
    print("========== Dictionary Operations ==========")
    states = {42: "Washington", 50: "Hawaii", 1: "Delaware"}
    print(states[42])  # Washington
    print(states[50])  # Hawaii

    # Adding to Dictionary
    emptyDict = {}
    emptyDict[1964] = "Pradip"
    emptyDict[1977] = "Supriya"
    emptyDict[1992] = "Unknown"
    emptyDict[1994] = "Abhijeet"
    emptyDict[1999] = "Arijeet"
    print(emptyDict)  # {1964: 'Pradip', 1977: 'Supriya', 1992: 'Unknown', 1994: 'Abhijeet', 1999: 'Arijeet'}

    # length of Dictionary
    print(len(emptyDict))  # 5

    # Reassign a value in Dictionary
    emptyDict[1992] = "Wedding of Pradip & Supriya"
    print(emptyDict)  # {1964: 'Pradip', 1977: 'Supriya', 1992: 'Wedding of Pradip & Supriya', 1994: 'Abhijeet', 1999: 'Arijeet'}

    # DELETING/ REMOVING a value
    del emptyDict[1992]
    print(emptyDict)  # {1964: 'Pradip', 1977: 'Supriya', 1994: 'Abhijeet', 1999: 'Arijeet'}


def flow_control_and_comparators():
    print("========== Flow Control and Comparators ==========")
    print(3 > 1)  # True
    print(5 >= 5)  # True
    print(1 == 7)  # False
    print(8 != 8)  # False


def list_operations():
    print("========== List Operaions ==========")
    ex1 = ["eggs", 1, "spam", 7.96]
    ex2 = []  # empty list

    # for accessing
    eggs = ex1[0]
    eggsSpam = ex1[0] + " " + ex1[2]
    ex1[1] = "sure"  # resetting value

    # Append: adds to the end of the list
    adder = [1, 2, 3, 4]
    print(adder)  # [1, 2, 3, 4]
    adder.append(5)
    print(adder)  # [1, 2, 3, 4, 5]

    # List slicing
    sliceEx = [9, 0, 2, 1, 0]
    print(sliceEx[:2])  # Means from 0 to 2: [9, 0]
    print(sliceEx[2:4])  # [2, 1]
    print(sliceEx[1:])  # [0, 2, 1, 0]

    # Index Function
    indexed = ["ab", "g", "gf", "bf"]
    print(indexed.index("gf"))  # sets the index number to firstZero, the first time it appears: in this case 2

    # Insert Function : adds value to anywhere
    inserted = ["Through", "Looking", "Glass"]
    inserted.insert(2, "the")
    print(inserted)  # ['Through', 'Looking', 'the', 'Glass']

    # remove function:
    removed = ["Need Stark", "Tony Stark", "Bran Stark"]
    removed.remove("Tony Stark")
    print(removed)  # ['Need Stark', 'Bran Stark']

    # pop function
    popped = ["Foo Fighters", "Green Day", "The White Strippers"]
    noDaveGroh1 = popped.pop(2)
    print(noDaveGroh1)  # The White Strippers
    print(popped)  # ['Foo Fighters', 'Green Day']
    noDaveGroh2 = popped.pop()  # removes the last element
    print(noDaveGroh2)  # Green Day

    # Range (their values cannot be reassigned like tuples, and append or insert will not work)
    range1 = range(8)  # [0,1,2,3,4,5,6,7]
    range2 = range(1, 4)  # [1,2,3]
    range3 = range(2, 20, 3)  # [2,5,8,11,14,17]
    for i in range(0, len(range3)):
        print(range3[i])

    # list of Lists!!
    listOfLists = [[1, 3, 5], [2, 4, 6]]
    print([i for i in listOfLists])  # [[1, 3, 5], [2, 4, 6]]
    print([i[0] for i in listOfLists])  # [1, 2]
    listOfLists_2 = [1, [2, 3], [4, 5, 6, 7], 8, 9]
    print(listOfLists_2[2][3])  # 7
    emptyList = []
    for each_list in listOfLists:
        for element in each_list:
            emptyList.append(element)
    print(emptyList)  # [1, 3, 5, 2, 4, 6]

    # List Comprehension
    example_list = [item for item in range(1, 10, 2)]
    print(example_list, end=" ")  # [1, 3, 5, 7, 9]
    print([num1 + 1 for num1 in range(10)])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ex2 = [num2 * 3 for num2 in range(1, 5)]  # ex2 = [3, 6, 9, 12, 15]
    ex3 = [num3 for num3 in range(10) if num3 % 2 == 0]  # ex3 = [0,2,4,6,8]
    ex4 = [num4 for num4 in range(0, 99, 3) if num4 % 3 == 0 and num4 % 5 == 0]  # ex4 = [0,15,30,45,60,75,90]

    # ===== Slice list using Stride =====
    exList = [num for num in range(1, 10)]  # exList = [1,2,3,4,5,6,7,8,9,10]
    sliced1 = exList[0:10:3]  # sliced1 = [1,4,7,10]
    sliced2 = exList[1:9:2]  # sliced2 = [2,4,6,8]
    sliced3 = exList[::2]  # sliced3 = [1,3,5,7,9]
    negSliced = exList[8:1:-2]  # negSliced = [9,7,5,3] # from 8 to 1 with decrementing 2, right to left
    reverseSliced = exList[::-1]  # reverseSliced = [10,9,8,7,6,5,4,3,2,1]


def loops_for_tuples():
    print("========== Loops for Tuples ==========")
    tuple1 = (5.6, "California", True, 1)
    tuple2 = 7, "Star Trek", 9.92, False
    emptyTuples = ()
    print(tuple2)  # (7, 'Star Trek', 9.92, False)

    # Accessing Tuples by Index
    print(tuple1[1])  # California

    # slicing Tuples
    print(tuple1[:3])  # (5.6, 'California', True)
    print(tuple1[1:4])  # ('California', True, 1)
    print(tuple1[2:])  # (True, 1)

    # ==================== For Loop ====================
    list1 = [1, 2, 3]
    print(*list1, end=" ")  # 1 2 3 4
    tuple3 = (4, 5, 6)
    print(*tuple3, end=" ")  # 4 5 6
    list_of_tuples = [(1, 2), (35, 8), (1, 4)]
    print(*list_of_tuples)  # [(1, 2), (35, 8), (1, 4)]
    list_index_1 = [item for item in list_of_tuples if item[0] == 35]
    list_index_2 = [item for item in list_of_tuples if 1 in item]
    print(list_index_1)  # [(35, 8)]
    print(list_index_2)  # [(1, 2), (1, 4)]

    # List
    listy = [4, 3, 2, 1, 0]
    emptyList = []
    for num in listy:
        emptyList.append(num * 5)
    print(emptyList)  # [20, 15, 10, 5, 0]

    # Tuple
    tup = ("Let", "It", "Be")
    song = ""

    for words in tup:
        song += words
    print(song)  # LetItBe

    # ==================== While Loop ====================
    counter = 0
    while counter < 5:
        print("something")
        counter += 1

    counter2 = 0
    while True:
        print("something again " + str(counter2))
        counter2 += 1
        if counter2 == 5:
            break

    counter3 = 0
    while counter3 < 5:
        print(counter3)
        counter3 += 1
    else:
        print(5)

    example_str = "example"
    print("=> Iterate through string: ")
    for char in example_str:
        print(char, end=" ")  # prints on the same line because if end="" : e x a m p l e
    print()
    print("=> Iterate through string using range: ")
    for char in range(len(example_str)):
        print(example_str[char], end=" ")  # e x a m p l e
    print()
    # Iterate through a dictionary
    ex_dict = {"first": 1, "second": 2, "third": 3}
    print("=> Iterate Through Dictionary: ", end="")
    for key in ex_dict:
        print(key + " " + str(ex_dict[key]), end=" ")  # first 1 second 2 third 3
    print()
    #  Zip Function
    list1 = [4, 0, 11, 3]
    list2 = [1, 1, 9, 18]
    print("=> Zip Function: ", end=" ")
    for items1, items2 in zip(list1, list2):
        if items1 > items2:
            print(items1, end=" ")  # 4 (1) 11 (18)
        elif items1 < items2:
            print(items2, end=" ")  # (4) 1 (11) 18


def main():
    # boolean_operators()
    # dictionary_operations()
    # flow_control_and_comparators()
    list_operations()
    # loops_for_tuples()


if __name__ == '__main__':
    main()
