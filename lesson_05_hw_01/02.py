from math import sqrt


def solve_quadratic_equation(a, b, c):
    d = b*b - 4*a*c
    if d < 0:
        x1 = None
        x2 = None
        return x1, x2
    elif d == 0:
        x1 = -b/2
        x2 = None
        return x1, x2
    else:
        x1 = (-b + sqrt(d)) / (2*a)
        x2 = (-b - sqrt(d)) / (2*a)
        return x1, x2


def main():
    a, b, c = map(int, input('Enter a b c with spaces: ').split())
    result = solve_quadratic_equation(a, b, c)
    if result[0] is None and result[1] is None:
        print('There are no solutions')
    elif result[1] is None:
        print(f'x = {result[0]:.2f}')
    else:
        print(f'x1 = {result[0]:.2f}, x2 = {result[1]:.2f}')


main()
