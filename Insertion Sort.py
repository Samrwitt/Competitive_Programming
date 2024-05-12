#!/bin/python3

import math
import os
import random
import re
import sys


def insertionSort1(n, arr):
    # Write your code here
    unsorted_num = arr[-1]
    i = n - 2
    while i >= 0 and arr[i] > unsorted_num:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
    arr[i + 1] = unsorted_num
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
