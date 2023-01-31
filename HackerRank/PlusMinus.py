""" 
Given an array of integers, calculate the ratios 
of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line 
with 6 places after the decimal.
"""

#!/bin/python3

import math
import os
import random 
import re 
import sys 

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positiveCount = 0
    negetiveCount = 0
    zeroCount = 0

    for i in range (len(arr)):
        if arr[i] > 0:
            positiveCount += 1
        elif arr[i] < 0 :
            negetiveCount +=1
        else:
            zeroCount += 1
            
    print("%f"%(positiveCount / len(arr)))
    print("%f"%(negetiveCount / len(arr)))
    print("%f"%(zeroCount / len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)