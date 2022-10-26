from math import sqrt


def solve_quadratic_equation(a, b, c):
    d = b*b - 4*a*c
    if d < 0:
        print('There are no solutions')
    elif d == 0:
        x = -b/2
        print(f'x = {x}')
    else:
        x1 = (-b + sqrt(d)) / (2*a)
        x2 = (-b - sqrt(d)) / (2*a)
        print(f'x1 = {x1:.2f}, x2 = {x2:.2f}')


def main():
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    solve_quadratic_equation(a, b, c)


main()
