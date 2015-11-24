from itertools import product
A = map(int,raw_input().split())
B = map(int,raw_input().split())
cartProd = list(product(A,B))
for i in cartProd: 
    print i,
print
