n = input()
s = set(map(int, raw_input().split())) 
N = int(raw_input())

for i in range(N):
    order = raw_input().split()
    command = order[0]
    if len(order)>1:
        value = int(order[1])
        
    if command == "remove" and value in s:
        s.remove(value)
       
    if command == "pop" and len(s)>0:
        s.pop()
    
    if command == "discard":
        s.discard(value)
        
print sum(s)