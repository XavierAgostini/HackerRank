bounds = map(int,raw_input().split())
nSize=bounds[0]
mSize=bounds[1]
N=(map(int,raw_input().split()))

A = set(map(int,raw_input().split()))
B = set(map(int,raw_input().split()))

happieness = 0
for i in range(0,nSize):
    if N[i] in A:
        happieness+=1
    if N[i] in B:
        happieness-=1
print happieness