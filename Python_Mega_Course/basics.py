address = ["Flat Floor Street", "18", "New York"]
address.append("USA")
address.append("This will be popped")
address.remove("USA")  # removes by matching
address.pop(-1)  # removed by index number
pins = {"Mike": 1234, "Joe": 1111, "Jack": 2222}

print(address[0], address[1])
# Flat Floor Street, 18

pin = int(input("Enter your pin: "))


def find_in_file(f):
    my_file = open("sample.txt")
    fruits = my_file.read()
    fruits = fruits.splitlines()
    if f in fruits:
        my_file.close()
        return "The fruit is in the list."
    else:
        return "No such fruit found!"


if pin in pins.values():
    fruit = input("Enter fruit: ")
    print(find_in_file(fruit))
else:
    print("Incorrect pin!")
    print("This info can be access only by: ")
    for key in pins.keys():
        print(key)
