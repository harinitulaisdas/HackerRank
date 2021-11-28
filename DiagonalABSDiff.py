def diagonal_absolute_sum(lst):
   sum  =0
   sum1 = 0
   for i in range(len(lst)):
       sum += lst[i][i]
   for i in range(len(lst)):
       sum1+= lst[i][len(lst)-i-1]
   return abs(sum-sum1)

if __name__ == '__main__':
    lst = [[11, 2 ,4],
           [4 ,5 ,6],
           [10, 8 ,-12]]
    print(diagonal_absolute_sum(lst))