def copydeep(lst):
    copy_lst = []
    for i in lst:
        if isinstance(i, list):
            copy_lst.append(copydeep(i))
        else:
            copy_lst.append(i)
    return copy_lst


def main():
    lst = ['a', 1, 2.0, ['b']]
    copy_lst = copydeep(lst)
    lst[3].append('0')
    print(f'lst = {lst}\ncopy_lst = {copy_lst}')


main()
