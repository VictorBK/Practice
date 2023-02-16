# A teacher asks the class to open their books to a page number. 
# A student can either start turning pages from the front of the book or from the back of the book. 
# They always turn pages one at a time. 
# When they open the book, page 1 is always on the right side.
# When they flip page 1, they see pages 2 and 3. 
# Each page except the last page will always be printed on both sides. 
# The last page may only be printed on the front, given the length of the book.
# If the book is n pages long, and a student wants to turn to page p,
# what is the minimum number of pages to turn? 
# NB: They can start at the beginning or the end of the book.

#!/bin/python3

import math
import os
import random
import re
import sys

#
#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    from_start = p//2
    from_end = n//2 - from_start
    return min(from_start, from_end)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()