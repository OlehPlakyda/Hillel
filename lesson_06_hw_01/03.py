from random import randint


def diff_odd_even(num_limit, lower_bound, upper_bound):  # returns int
    odd = 0
    even = 0
    for _ in range(num_limit):
        a = randint(lower_bound, upper_bound)
        if a % 2 == 0:
            even += a
        else:
            odd += a
    return even - odd


def main():
    num_limit = int(input('Enter amount of numbers: '))
    lower_bound, upper_bound = map(int, input('Enter lower_bound and upper_bound with spaces: ').split())
    print('Difference between sums even and odd numbers = ', diff_odd_even(num_limit, lower_bound, upper_bound))


main()
