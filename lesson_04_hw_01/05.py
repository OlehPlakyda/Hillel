def printtask(list):
    print(list[2])
    print(list[-2])
    print(''.join(list[0:5]))
    print(''.join(list[0:-2]))
    n = len(list)
    for x in range(0, n, 2):
        print(list[x], end=' ')
    print()
    for y in range(1, n, 2):
        print(list[y], end=' ')
    print()
    for z in range(n-1, -1, -1):
        print(list[z], end=' ')
    print()
    for z in range(n - 1, -1, -2):
        print(list[z], end=' ')
    print('\nLength of the string =', n)


string = input('Enter a string: ')
list = [*string]
printtask(list)
