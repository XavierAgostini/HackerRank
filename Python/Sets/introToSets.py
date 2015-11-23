from __future__ import division

T = int(raw_input())
plantHeights = set(map(int, raw_input().split()))

average = sum(plantHeights)/len(plantHeights)

print average
