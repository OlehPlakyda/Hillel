def fibonacci_by_number(number, a):
    n = len(a)
    a.append(a[n-1] + a[n-2])
    if n+1 == number:
        print(a[n])
        return
    return fibonacci_by_number(number, a)


def main():
    number = int(input('Enter a number: '))
    a = [0, 1]
    fibonacci_by_number(number, a)


main()
