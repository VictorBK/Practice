# There will be two arrays of integers.
# Determine all integers that satisfy the following two conditions:
# 1. The elements of the first array are all factors of the integer being considered.
# 2. The integer being considered is a factor of all elements of the second array.
# These numbers are referred to as being between the two arrays. 
# Determine how many such numbers exist.
# Example: a = [2,6] and b = [24,36]
# There are two numbers between the arrays: 6 and 12.
# 6%2 = 0, 6%6 = 0, 24%6 = 0, and 36%6 = 0 for the first value.
# 12%2 = 0, 12%6 = 0, and 24%12 = 0, 36%12 = 0 for the second value.
# Return 2.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def gcd(a,b):
    # Return greatest common divisor using Euclid's Algorithm.
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    # Return lowest common multiple.
    return a * b / gcd(a, b)

def GCD(terms):
    # Return gcd of a list of numbers.
    ans = terms[0]
    for i in range(1, len(terms)):
        ans = gcd(ans, terms[i])
    return ans

def LCM(terms):
    # Return lcm of a list of numbers.
    ans = 1
    for t in terms:
        ans = lcm(ans, t)
    return ans

def getTotalX(a, b):
    lcm_value = LCM(a)
    gcd_value = GCD(b)
    count = 0
    multiple_lcm = lcm_value
    while multiple_lcm <= gcd_value:
        if (gcd_value % multiple_lcm) == 0:
            count += 1
        multiple_lcm += lcm_value
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
