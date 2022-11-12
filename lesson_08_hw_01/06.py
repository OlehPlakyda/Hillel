import random


def pemrtuate(text):
    lst = text.split()
    copy_lst = ['first_symbol', 'middle_part', 'last_symbol']
    symbols = [':', '?', '.', '!', ',', "'", '"']
    for i in range(0, len(lst)-1):
        if len(lst[i]) > 3:
            if lst[i][0] in symbols and lst[i][-1] in symbols:
                copy_lst[0] = lst[i][0] + lst[i][1]
                copy_lst[1] = lst[i][2:-2]
                copy_lst[2] = lst[i][-2] + lst[i][-1]
            elif lst[i][0] in symbols:
                copy_lst[0] = lst[i][0] + lst[i][1]
                copy_lst[1] = lst[i][2:-1]
                copy_lst[2] = lst[i][-1]
            elif lst[i][-1] in symbols:
                copy_lst[0] = lst[i][0]
                copy_lst[1] = lst[i][1:-2]
                copy_lst[2] = lst[i][-2] + lst[i][-1]
            else:
                copy_lst[0] = lst[i][0]
                copy_lst[1] = lst[i][1:-1]
                copy_lst[2] = lst[i][-1]
            copy_lst[1] = ''.join(random.sample(copy_lst[1], k=len(copy_lst[1])))
            lst[i] = ''.join(copy_lst)
    return ' '.join(lst)


def main():
    text = 'Украї́на — держава, розташована у Східній Європі, охоплює південний захід Східноєвропейської рівнини, ' \
           'частину Східних Карпат і Кримські гори.'
    print(text)
    print(pemrtuate(text))


main()
