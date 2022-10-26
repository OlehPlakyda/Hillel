def is_even(number):  # returns boolean value
    return number % 2 == 0


def main():
    number = int(input('Enter a number: '))
    print(is_even(number))


main()
