def counting_sort(arr):
    frq_arr =[0]*100
    for i in range(len(arr)):
        frq_arr[arr[i]]+=1
    print(frq_arr)

if __name__=='__main__':
    arr =[1, 1, 3, 2, 1]

    counting_sort(arr)
