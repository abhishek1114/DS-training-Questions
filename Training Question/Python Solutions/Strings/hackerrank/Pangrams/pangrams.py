#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    s = set(s)
    s.discard(" ")
    l = [int(a) for a in range(65,91)]
    for ch in s:
        # print(ord(ch))
        if ord(ch) in l:
            l.remove(ord(ch))
        elif ord(ch)-32 in l:
            l.remove(ord(ch)-32)
    # print(l)
    if len(l)==0:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
