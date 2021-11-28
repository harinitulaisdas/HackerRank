def plus_minus(arr):
    print((len([x for x in arr if x > 0]) / len(arr)).__format__('.6f'))
    print((len([x for x in arr if x < 0]) / len(arr)).__format__('.6f'))
    print((len([x for x in arr if x == 0]) / len(arr)).__format__('.6f'))

if __name__ == '__main__':
    arr = [1, 1, 0, -1, -1]
    plus_minus(arr)
