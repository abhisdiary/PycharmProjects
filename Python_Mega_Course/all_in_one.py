# =================== Python Dictionary ===================
def dictionary_test():
    dictionary_id = {"id": 13301130, "full_name": "null", "first_name": "Abhijeet", "surname": "Roy", "age": 25}
    print(dictionary_id)
    # {'id': 13301130, 'full_name': 'null', 'first_name': 'Abhijeet', 'surname': 'Roy', 'age': 25}
    dictionary_id.pop("surname")
    print(dictionary_id)
    # {'id': 13301130, 'full_name': 'null', 'first_name': 'Abhijeet', 'age': 25}
    dictionary_id["full_name"] = "Abhijeet Roy"
    print(dictionary_id)
    # {'id': 13301130, 'full_name': 'Abhijeet Roy', 'first_name': 'Abhijeet', 'age': 25}
    print(dictionary_id["id"])
    # 13301130
    print(dictionary_id.keys())
    # dict_keys(['Mike', 'Joe', 'Jack'])
    print(dictionary_id.values())
    # dict_values([13301130, 13301129, 45673535])
    # === Mapping 2 Lists to a dictionary ===
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    my_dict = dict(zip(keys, values))
    print(my_dict)
    # {'a': 1, 'b': 2, 'c': 3}


# ==================== Python Read Files ====================
def file_read_test():
    file = open("sample.txt")
    my_file = file.read()
    print(my_file)
    # apple
    # banana
    # orange
    # peer
    file2 = open("sample_folder/sample_file.txt")
    my_file2 = file2.read()
    print(my_file2.splitlines())
    file2.close()
    print("apple" in my_file)
    # True
    for line in my_file.splitlines():
        print(len(line))


# ==================== Python Write Files ====================
def file_write_test():
    my_file = open("sample_folder/new_text_file.txt", "w")
    my_file.write("Mike")  # write method only takes string. Integers & others have to be converted to string
    my_file.close()  # closing is important for changes to take place
    # You can also use the following way (Recommended)

    # with open("example.txt", "w") as my_file:
    #   my_file.write("Mike")


# ==================== Python Append Files ====================
def file_append_test():
    my_file = open("sample_folder/new_text_file.txt", "a")
    my_file.write("\nJack")
    my_file.close()
    # print(my_file.read()) # Will not run, because append mode can not read


# ==================== Python Read and Append Files ====================
def file_append_and_read():
    my_file = open("sample.txt", "a+")
    print(my_file.read())


# ==================== While Loop ====================
def while_loop():
    correct_password = "python"
    name = input("Enter your name: ")
    sur_name = input("Enter your surname: ")
    password = input("Enter password: ")

    while password != correct_password:
        password = input("Wrong Password! Enter password again: ")

    print("Hi", name, "you are logged in!")
    print("%s %s Enjoy the Freedom" % (name, sur_name))


# ==================== Python Read and Append Files ====================
def zip_function():
    a = ['a', 'b', 'c']
    b = [1, 2, 3]
    for i, j in zip(a, b):
        print("%s is %s" % (i, j))


# ==================== Main Test File ====================
def main():
    # dictionary_test()
    # file_read_test()
    # file_write_test()
    # file_append_test()
    # file_append_and_read()
    # while_loop()
    zip_function()


if __name__ == '__main__':
    main()
