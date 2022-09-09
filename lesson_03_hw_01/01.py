# a) with the help of c

print('First variant:')

a = 3
b = 8

print('At the start of the program:', '\na =', a, '\nb =', b)

c = a
a = b
b = c

print('At the end of the program:', '\na =', a, '\nb =', b)

# b) without help

print('\nSecond variant:')

a = 'space'
b = 'star'

print('At the start of the program:', '\na =', a, '\nb =', b)

a, b = b, a

print('At the end of the program:', '\na =', a, '\nb =', b)

# c) with the help of '+' and '-'

print('\nThird variant:')

a = 3
b = 8

print('At the start of the program:', '\na =', a, '\nb =', b)

a += b
b = a - b
a -= b

print('At the end of the program:', '\na =', a, '\nb =', b)