def degrees2radians(degrees):  # returns float: radians value
    radians = 3.14/180 * degrees
    print(round(radians, 2))
    return radians


degrees = int(input('Enter degrees: '))
degrees2radians(degrees)
