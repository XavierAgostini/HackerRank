a = int(raw_input())
set1 = set(map(int,raw_input().split()))
b = int(raw_input())
set2 = set(map(int,raw_input().split()))
finalSet = set()
finalSet.update(set1.difference(set2))
finalSet.update(set2.difference(set1))
sortedSet =  sorted(finalSet)
for x in sortedSet:
    print x