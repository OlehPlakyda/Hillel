def fibonacci_by_number(number, a=[0, 1]):
    n = len(a)
    a.append(a[n-1] + a[n-2])
    if n+1 == number or number < n+1:
        return a
    return fibonacci_by_number(number, a)


def main():
    number = int(input('Enter a number: '))
    a = fibonacci_by_number(number)
    print(a[number-1])


main()
