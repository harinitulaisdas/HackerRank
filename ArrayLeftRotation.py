def rotate_array(arr,n):
    arr1 = [arr[i] for i in range(n,len(arr))] + [arr[i] for i in range(0,n)]
    print(arr1)



if __name__=='__main__':
    n = int(input("enter n: ").strip())
    arr = [1,2,3,4,5,6]
    rotate_array(arr,n)