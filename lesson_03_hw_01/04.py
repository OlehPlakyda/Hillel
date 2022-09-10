a = input('Enter first name, last name, date of birth and death: ')

a = a.split('*')
b = a[1].split('-')
c = a[2].split('-')
age = int(c[0]) - int(b[0])

print('Name:', a[0])
print('Age:', age, 'years')
