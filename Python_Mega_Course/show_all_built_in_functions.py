print(dir(__builtins__))
print()
print("Now Printing One by one: ")
print()

for f in dir(__builtins__):
    print(f)

print()
print("Now Ask python to know what a function does: ")
print("For that use 'help(function_name)'")
print()
print(help(len))
print()
print("==============================================")
print()
print("Now we will see how to know which functions I can apply on an object: ")
a_list = ["Guddu", "Muddu", "Pokke", "Kakka"]
print(dir(a_list))
a = 10
print(dir(a))
