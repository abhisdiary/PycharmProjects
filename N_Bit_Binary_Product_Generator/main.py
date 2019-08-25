import itertools


def without_built_in_functions(total_bits):
    binary_bits = [0, 1]
    print([(x, y, z) for x in binary_bits for y in binary_bits for z in binary_bits])


def with_built_in_function(total_bits):
    lst = list(itertools.product([0, 1], repeat=total_bits))
    print(*lst, sep="\n")
    print("Total Combinations: ", len(lst))
    lsb_2_bits_11 = [i for i, v in enumerate(lst) if v[0] == 1 & v[1] == 1]
    print(*lsb_2_bits_11, sep="\n")


def main():
    # without_built_in_functions(3)
    with_built_in_function(8)


if __name__ == '__main__':
    main()
