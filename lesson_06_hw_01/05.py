def calculate_wheat_chess_position(kilograms):
    n = 0
    for n in range(65):
        weight = 1 * 2**(n-1) * 0.000035
        if weight >= kilograms:
            break
    for i in 'abcdefgh':
        if n <= 8:
            return f'{i}{n}'
        n -= 8


def main():
    kilograms = float(input('Enter the weight of the grain in kilograms: '))
    print('Your position in chess:', calculate_wheat_chess_position(kilograms))


main()
