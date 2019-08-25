ex1 = ["eggs", 1, "spam", 7.96]
ex2 = []  # empty list

# for accessing
eggs = ex1[0]

eggsSpam = ex1[0] + " " + ex1[2]
ex1[1] = "sure"

# Append: adds to the end of the list
adder = [1, 2, 3, 4]
print(adder)
adder.append(5)
print(adder)

# List slicing
sliceEx = [9, 0, 2, 1, 0]

slice1 = sliceEx[:2]  # Means from 0 to 2
slice2 = sliceEx[2:4]
slice3 = sliceEx[1:]

# Index Function
indexed = ["ab", "g", "gf", "bf"]
firstZero = indexed.index("gf")  # sets the index number to firstZero, the first time it appears

# Insert Function : adds value to anywhere
inserted = ["Through", "Looking", "Glass"]
inserted.insert(2, "the")

# remove function:
removed = ["Need Stark", "Tony Stark", "Bran Stark"]
removed.remove("Tony Stark")

# pop function
popped = ["Foo Fighters", "Green Day", "The White Stripers"]
noDaveGroh1 = popped.pop(2)
noDaveGroh2 = popped.pop()  # removes the last element

# Range (their values cannot be reassigned like tuples, and append or insert will not work)
range1 = range(8)  # [0,1,2,3,4,5,6,7]
range2 = range(1, 4)  # [1,2,3]
range3 = range(2, 20, 3)  # [2,5,8,11,14,17]
for x in range(0, len(range3)):
    print(range3[x])

# list of Lists!!
listOfLists = [[1, 3, 5], [2, 4, 6]]
emptyList = []
for list in listOfLists:
    for element in list:
        emptyList.append(element)
print(emptyList)

# List Comprehension
print("========== List Comprehensions: ==========")
example_list = [item for item in range(1, 10, 2)]
print(example_list, end=" ")
ex1 = [num1 + 1 for num1 in range(10)]
# ex1 = [1,2,3,4,5,6,7,8,9,10]
ex2 = [num2 * 3 for num2 in range(1, 5)]
# ex2 = [3, 6, 9, 12, 15]
ex3 = [num3 for num3 in range(10) if num3 % 2 == 0]
# ex3 = [0,2,4,6,8]
ex4 = [num4 for num4 in range(0, 99, 3) if num4 % 3 == 0 and num4 % 5 == 0]
# ex4 = [0,15,30,45,60,75,90]

# ===== Slice list using Stride =====
exList = [num for num in range(1, 10)]
# exList = [1,2,3,4,5,6,7,8,9,10]
sliced1 = exList[0:10:3]
# sliced1 = [1,4,7,10]
sliced2 = exList[1:9:2]
# sliced2 = [2,4,6,8]
sliced3 = exList[::2]
# sliced3 = [1,3,5,7,9]
negSliced = exList[8:1:-2]
# negSliced = [9,7,5,3] # from 8 to 1 with decrementing 2, right to left
reverseSliced = exList[::-1]
# reverseSliced = [10,9,8,7,6,5,4,3,2,1]
