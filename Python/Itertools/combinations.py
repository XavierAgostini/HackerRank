from itertools import combinations
S,k = raw_input().split()
k = int(k)
for i in range(0,k):
    for j in list(combinations(sorted(S),i+1)):
        print ''.join(j)
