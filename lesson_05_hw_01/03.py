from math import sqrt


def circles_intersect(x1, y1, r1, x2, y2, r2):  # returns boolean value
    r = r1 + r2
    d = sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
    return r >= d


def main():
    x1, y1, r1 = map(int, input('Enter x1 y1 r1 with spaces: ').split())
    x2, y2, r2 = map(int, input('Enter x2 y2 r2 with spaces: ').split())
    if circles_intersect(x1, y1, r1, x2, y2, r2) is True:
        print('These circles intersect')
    else:
        print('These circles don`t intersect')


main()
