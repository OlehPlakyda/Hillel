def sum_symbol_codes(first, last):
    a = [ord(first)]
    while a[-1] < ord(last):
        a.append(a[-1] + 1)
    return sum(a)


def main():
    first, last = input('Enter first and last symbol with spaces: ').split()
    print('Your sum is', sum_symbol_codes(first, last))


main()
