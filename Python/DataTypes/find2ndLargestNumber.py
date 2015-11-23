N = int(raw_input())
A = map(int,raw_input().split())

largest = max(A)
B = [x for x in A if x!=largest]
secondLargest = max(B)    
print secondLargest