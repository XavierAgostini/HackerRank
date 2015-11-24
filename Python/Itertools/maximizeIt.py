from itertools import product
K,M = map(int,raw_input().split())
s = []

for i in range(K):
    s.append(map(int,raw_input().split()[1:]))

f = map(sum,[map(lambda x: x**2, i) for i in list(product(*s))])
t = map(lambda x: x%M, f)
print max(t)
