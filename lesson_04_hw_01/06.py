def my_sum(*num, start=0):
    my_sum = sum(num, start)
    return my_sum


print('Your sum is:', my_sum(1, 2, 3, 4, 5, 6, start=60))
