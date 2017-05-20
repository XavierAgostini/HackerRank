#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

totP = totN = tot0 = 0
for el in arr:
    if el < 0: totN += 1
    elif el == 0: tot0 +=1
    else: totP +=1
print('{0:.6}'.format(totP/n))
print('{0:.6}'.format(totN/n))
print('{0:.6}'.format(tot0/n))