def index(lst, elem):  # returns integer or None
    for idx, element in enumerate(lst):
        if elem == element:
            return idx
    return None


def main():
    lst = ['a', 'b', 'c', 'd', 'e', 'f']
    elem = 'f'
    print(index(lst, elem))


main()
