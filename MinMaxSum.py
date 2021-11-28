def min_max_sum(arr):
    arr.sort()
    summ,summ1 = 0,0
    for i in range(len(arr)-1):
        summ += arr[i]
    print(summ)
    for i in range(1,len(arr)):
        summ1 += arr[i]
    print(summ1)
if __name__ == '__main__':
    arr = [1,3,5,7,9]
    min_max_sum(arr)
