#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
#arr = [5, 4, 3, 2, 1]

def miniMax(arr):
    sum = 0
    # sort arr
    for i in range(0, len(arr)):    
        for j in range(0, len(arr)):  
            if j < len(arr) - 1 and arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    sum = arr[0] + arr[1] + arr[2] + arr[3] + arr[4]
    print(sum - arr[4], sum-arr[0])
miniMax(arr)
