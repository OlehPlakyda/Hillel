from random import randint


def random_12digit_number():
    return randint(100000000000, 999999999999)


def get_max_digit(number):  # returns int
    x = 0
    for i in range(12):
        a = number % 10
        if a > x:
            x = a
        number //= 10
    return x


def main():
    number = random_12digit_number()
    print('A randomly generated 12-digit number: ', number)
    print('The largest digit of this number: ', get_max_digit(number))


main()
