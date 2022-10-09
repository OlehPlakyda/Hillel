def my_sum(num, start=0):
    sum = 0
    n = len(num)
    for i in range(n):
        sum += int(num[i-1])
    sum += start
    print('Your sum is:', sum)


num = input('Enter a number: ')
num = [*num]
start = int(input('Enter a number start: '))
my_sum(num, start)
