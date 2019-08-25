tuple1 = (5.6, "California", True, 1)
tuple2 = 7, "Star Trek", 9.92, False
emptyTuples = ()

# Accessing Tuples by Index
print(tuple1[1])

# slicing Tuples
first3 = tuple1[:3]
mid3 = tuple1[1:4]
last3 = tuple1[2:]

# ==================== For Loop ====================
list1 = [1, 2, 3]
tuple3 = (4, 5, 6)

for elements in list1:
    print(elements)

for items in tuple1:
    print(items)

# List
listy = [4, 3, 2, 1, 0]
emptyList = []

# Tuple
tup = ("Let", "It", "Be")
song = ""

for num in listy:
    emptyList.append(num * 5)

for words in tup:
    song += words

print(emptyList)
print(song)

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
    print(char, end=" ")  # prints on the same line because if end=""
print()
print("=> Iterate through string using range: ")
for char in range(len(example_str)):
    print(example_str[char], end=" ")

print()
# Iterate through a dictionary
ex_dict = {"first": 1, "second": 2, "third": 3}
print("=> Iterate Through Dictionary: ", end="")
for key in ex_dict:
    print(key + " " + str(ex_dict[key]), end=" ")

print()
#  Zip Function
list1 = [4, 0, 11, 3]
list2 = [1, 1, 9, 18]
print("=> Zip Function: ", end=" ")
for items1, items2 in zip(list1, list2):
    if items1 > items2:
        print(items1, end=" ")
    elif items1 < items2:
        print(items2, end=" ")
