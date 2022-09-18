def triangle_square_and_perimeter(a, b):  # returns 2 values
    global s, p
    s = a * b * 0.5
    p = (a**2 + b**2)**0.5 + a + b


s, p = 0, 0
a = int(input('Enter the length of the first leg: '))
b = int(input('Enter the length of the second leg: '))
triangle_square_and_perimeter(a, b)
print('square =', s, '\nperimeter =', p)
