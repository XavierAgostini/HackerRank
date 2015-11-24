from itertools import combinations_with_replacement
S,k = raw_input().split()
for i in list(combinations_with_replacement(sorted(S),int(k))):
    print ''.join(i)
