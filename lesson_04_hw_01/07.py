def my_sum(num):
    sum = ord(num[0]) + ord(num[1]) + ord(num[2]) - 144
    return(sum)


num = input('Enter a three-digit number: ')
if len(num) > 3:
    print('Error: Your number has more than three digits')
else:
    my_sum(num)
