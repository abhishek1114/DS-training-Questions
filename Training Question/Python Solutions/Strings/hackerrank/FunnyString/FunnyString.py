#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    c=0
    r = s[::-1]
    l1 = [abs(ord(s[i+1])-ord(s[i])) for i in range(len(s)-1) ]
    l2 = [abs(ord(r[i+1])-ord(r[i])) for i in range(len(s)-1) ]
    for i in range(len(l1)):
        if l1[i]==l2[i]:
            c=0
        else:
            c=1
            break
    if c==0:
        return 'Funny'
    else:
        return 'Not Funny'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
