def leap_year(x):
    if x % 400 == 0:
        print(f'{x} is a leap year')
    elif x % 4 == 0 and x % 100 != 0:
        print(f'{x} is a leap year')
    else:
        print(f'{x} isn`t a leap year')


def main():
    x = int(input('Enter a natural number: '))
    leap_year(x)


main()
