#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    def hourglassSum(arr):
        # Write your code here
        print(arr)

        hsumlist = []
        for i in range(4):
            hsum = 0
            for j in range(4):
                hsum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
                hsum += arr[i + 1][j + 1]
                hsum += arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
                hsumlist.append(hsum)

        hsumlist.sort()
        return hsumlist[-1]



