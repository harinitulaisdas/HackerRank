from collections import Counter
from functools import reduce


def lonely_integer(arr):
    cnt_val = Counter(arr)
    unique_val = 0
    #method1 bitwise xor
    lonely_integer = reduce(lambda x, y: x ^ y, arr)
    print("{} is the lonely integer".format(lonely_integer))

    #Method 2j
    for i in cnt_val:
        unique_val = i if cnt_val[i] == 1 else None
    return 'No unique element found' if unique_val == None else '{} is the unique element'.format(unique_val)


if __name__=='__main__':
    arr = [1, 2, 2, 1, 3, 4, 4,3,5]
    print(lonely_integer(arr))

