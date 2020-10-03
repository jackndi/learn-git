
def main():
    print("Main")


def is_even(number):
    """ check is the number is even"""
    return True if number % 2 == 0 else False


if __name__ == "__main__":
    main()

    # test the is_even
    print("1 ", is_even(1))
    print("4 ", is_even(4))
