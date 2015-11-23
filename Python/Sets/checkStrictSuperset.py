A = set(raw_input().split())
state = True
for i in range(int(raw_input())):
    if set(raw_input().split()).issubset(A): 
        state = True
    else: 
        state = False
        break
print state
        
