def birthday_cake_candles(arr):
    arr.sort()
    max_height,count  = 0,0
    max_height = arr[len(arr) - 1]
    for i in range(len(arr)):
        if arr[i]==max_height:
            count+=1

    print(max_height , '', count)

if __name__ == '__main__':
    arr = [3, 2, 1, 3]
    birthday_cake_candles(arr)
