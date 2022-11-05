from random import randint


def game_hidden_number():
    x = randint(1, 10)
    print('\nThe program hide the number(from 1 to 10). Try to guess it \U0001F609')
    a = int(input('Enter the number: '))
    while a != x:
        if a < x:
            print(f'\nThe hidden number is greater than {a}')
        else:
            print(f'\nThe hidden number is less than {a}')
        a = int(input('Try one more time \U0001F914 Enter the number: '))
    print('\nCongratulations \U0001F92F You guessed the number \U0001F973')
    start_end = input('\nDo you want to play one more time?(+/-): ')
    if start_end == '+':
        game_hidden_number()
    elif start_end == '-':
        print('\nThe end \U0001f480')
        pass


def main():
    start_end = input('Do you want to start a game?(+/-): ')
    if start_end == '+':
        print('\nLet`s start \U0001f601')
        game_hidden_number()
    elif start_end == '-':
        print('\nThe end \U0001f480')


main()
