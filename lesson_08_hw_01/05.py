def gen_primes():
    lst = [2]
    rule = 0
    for i in range(3, 101):
        for j in lst:
            if i % j != 0:
                rule = True
            else:
                rule = False
                break
        if rule is True:
            lst.append(i)
    return lst


def main():
    print(gen_primes())


main()
