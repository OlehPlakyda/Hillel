def fibonacci_by_number(number, a=None):
    if a is None:
        a = [0, 1]
    n = len(a)
    a.append(a[n-1] + a[n-2])
    if n+1 == number or number < n+1:
        return a[number-1]
    return fibonacci_by_number(number, a)


def main():
    number = int(input('Enter a number: '))
    print(fibonacci_by_number(number))


main()
