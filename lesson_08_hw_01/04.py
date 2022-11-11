import random


def password_generator(length=8):
    digits = '0123456789'
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    combined_chars = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password = ''
    password += random.choice(upper_case)
    password += random.choice(lower_case)
    password += random.choice(digits)
    for i in range(3, length):
        password += random.choice(combined_chars)
    for i in range(1, length-1, 2):
        while password[i-1] == password[i] == password[i+1]:
            password.replace(password[i], random.choice(combined_chars))
    return ''.join(random.sample(password, k=length))


def main():
    for i in range(10):
        print(password_generator())


main()
