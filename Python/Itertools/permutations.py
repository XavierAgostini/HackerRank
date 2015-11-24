from itertools import permutations
command = raw_input().split()
S = sorted(command[0])
k = int(command[1])
for i in list(permutations(S,k)):
    print ''.join(i), " "
