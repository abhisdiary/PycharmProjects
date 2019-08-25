from datetime import datetime
import glob2

"""
My task is to read all the files inside the sample_folder and
merge them into a new file named with the current timestamp, inside the folder merged_file.
"""

file_names = glob2.glob("sample_folder/*.txt")


def merge_files():
    with open("merged_file/" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", 'w') as merged_file:
        for file_name in file_names:
            with open(file_name, "r") as f:
                merged_file.write(f.read() + "\n")


def main():
    merge_files()


if __name__ == '__main__':
    main()
