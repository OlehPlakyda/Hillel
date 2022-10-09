def my_sum(num):
    total = ord(num[0]) + ord(num[1]) + ord(num[2]) - 144
    print('Your sum is:', total)


num = input('Enter a three-digit number: ')
if len(num) > 3:
    print('Error: Your number has more than three digits')
else:
    my_sum(num)
