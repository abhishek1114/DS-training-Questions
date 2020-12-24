#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    lst = []
    for i in range(len(arr)):
        a = arr[i]
        summ = sum(arr)-a
        lst.append(summ)
    print(min(lst),max(lst))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
