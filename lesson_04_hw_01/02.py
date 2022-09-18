import math


def degrees2radians(degrees):  # returns float: radians value
    radians = 3.14/180 * degrees
    return radians


print(round(math.cos(degrees2radians(60)), 2))
print(round(math.cos(degrees2radians(45)), 2))
print(round(math.cos(degrees2radians(40)), 2))
