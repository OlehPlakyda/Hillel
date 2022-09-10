b = input('Enter a string variable in snake_case format: ')

b = str.title(b)
b = b.split('_')
b = ''.join(b)

print(b)
