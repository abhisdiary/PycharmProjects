def error_handle_test(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Not possible to divide %s with %s" % (a, b)


def main():
    print(error_handle_test(1, 0))


if __name__ == '__main__':
    main()
