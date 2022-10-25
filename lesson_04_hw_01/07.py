def my_sum(num):
    sum = ord(num[0]) + ord(num[1]) + ord(num[2]) - 144
    return sum


num = input('Enter a three-digit number: ')
length = len(num)
if length > 3 or length < 3:
    print('Error: Your number is incorrect')
else:
    print('Your sum is', my_sum(num))
