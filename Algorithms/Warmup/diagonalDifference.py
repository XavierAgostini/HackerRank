#!/bin/python3

import sys


def diagonalDiff(arr):
    primeD = secD = 0
    for i in range(0, len(arr)):
        primeD += arr[i][i]
        secD += arr[len(arr)-1-i][i]
    return abs(primeD - secD)
    
n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

print(diagonalDiff(a))