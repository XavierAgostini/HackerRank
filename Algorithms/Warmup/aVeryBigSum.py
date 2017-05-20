#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
sum = 0
for elem in arr:
    sum += elem
print sum