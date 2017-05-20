#!/bin/python3

import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

height.sort()
tot = 0
for i in range(0, len(height)):
    if height[i] == height[-1]: tot += 1
print(tot)