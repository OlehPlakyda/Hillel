def sign(x):
    if x > 0:
        s = 1
    elif x < 0:
        s = -1
    else:
        s = 0
    return s


def main():
    x = int(input('Enter a number: '))
    print(f'sign(x) = {sign(x)}')


main()
