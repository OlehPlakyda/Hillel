def main():
    orig_lst = [5, '9', 0, '452', 6.5, '6', 1, 2]
    print('Original list: ', orig_lst)
    print('Sorted list a: ', sorted(orig_lst, key=float))
    print('Sorted list b: ', sorted(orig_lst, key=str))


main()
