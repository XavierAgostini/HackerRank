from collections import defaultdict
d = defaultdict(list) 
numWords = map(int,raw_input().split())
A = numWords[0]
B = numWords[1]
aWords= []
bWords=[]
final=[]
for i in range(0,A):
    aWords.append(raw_input())
for i in range(0,B):
    bWords.append(raw_input())
    #b = raw_input()
    #if b not in bWords: bWords.append(b)
for b in bWords:
    if b not in d:
        for i in range(0,A):
            if aWords[i]==b:
                d[b].append(i+1)   
        if len(d[b])==0: d[b].append(-1)
        for x in d[b]: print x,
        print
    else:
        for x in d[b]: print x,
        print
        