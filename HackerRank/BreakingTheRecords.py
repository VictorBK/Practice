# Maria plays college basketball and wants to go pro.
# Each season she maintains a record of her play.
# She tabulates the number of times she breaks her season record for most points and least points in a game.
# Points scored in the first game establish her record for the season, and she begins counting from there.
# Example: Scores = [12,24,10,24]
# Scores are in the same order as the games played. She tabulates her results as follows:
#                                       Count
# Game  Score   Minimum Maximun        Min      Max
#   0      12       12      12          0       0
#   1      24       12      24          0       1
#   2      10       10      24          1       1
#   3      24       10      24          1       1
# Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    maxi = scores[0]
    mini = scores[0]
    max_count = 0
    min_count = 0
    for i in range(len(scores)):
        if(scores[i] > maxi):
            maxi = scores[i]
            max_count += 1
        if(scores[i] < mini):
            mini = scores[i]
            min_count += 1
    return [max_count, min_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()