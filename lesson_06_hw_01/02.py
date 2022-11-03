from random import randint


def diff_min_max(num_limit, lower_bound, upper_bound):  # returns int
    a = []
    for _ in range(num_limit):
        a.append(randint(lower_bound, upper_bound))
    return max(a) - min(a)


def main():
    num_limit = int(input('Enter amount of numbers: '))
    lower_bound, upper_bound = map(int, input('Enter lower_bound and upper_bound with spaces: ').split())
    print('Difference between min and max number:', diff_min_max(num_limit, lower_bound, upper_bound))


main()
