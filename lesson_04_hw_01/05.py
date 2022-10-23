def printTask(string):
    print(string[2])
    print(string[-2])
    print(string[0:5])
    print(string[0:-2])
    print(string[::2])
    print(string[1::2])
    print(string[::-1])
    print(string[::-2])
    n = len(string)
    print('Length of the string =', n)


string = input('Enter a string: ')
printTask(string)
