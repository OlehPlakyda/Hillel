def triangle_square_and_perimeter(a, b):  # returns 2 values
    square = a * b * 0.5
    perimeter = (a**2 + b**2)**0.5 + a + b
    return (square, perimeter)


a = int(input('Enter the length of the first leg: '))
b = int(input('Enter the length of the second leg: '))
c = triangle_square_and_perimeter(a, b)
print('square =', c[0], '\nperimeter =', c[1])
