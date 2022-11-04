from random import randint


def random_12digit_number():
    return randint(100000000000, 999999999999)


def get_max_digit(number):  # returns int
    number = str(number)
    print(number)
    for i in range(9, 1, -1):
        if f'{i}' in number:
            return i


def main():
    number = random_12digit_number()
    print('The largest digit of a randomly generated 12-digit number = ', get_max_digit(number))


main()
