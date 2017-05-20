#!/bin/python3

import sys

time = input().strip()

milTime = time[:-2]
amPm = time[-2:]

if amPm == "PM":
    tempTime = int(milTime[0]+milTime[1]) + 12
    if tempTime == 24: tempTime = 12
    milTime = str(tempTime) + milTime[2:]
elif amPm == "AM":
    tempTime = int(milTime[0]+milTime[1])
    if tempTime == 12: 
        tempTime = "00"
        milTime = str(tempTime) + milTime[2:]
print(milTime)