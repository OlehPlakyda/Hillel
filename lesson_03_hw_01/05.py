a = input('Enter a three-digit number: ')
b = int(a)

# a) Using strings

a = int(a[0]) + int(a[1]) + int(a[2])

print('Exit number in variant a:', a)

# b) Using number

b1 = b//10
b = b % 10 + b1 % 10 + b1//10

print('Exit number in variant b:', b)
