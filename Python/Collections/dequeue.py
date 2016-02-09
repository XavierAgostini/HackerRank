# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
q = deque()
for i in range(0,int(raw_input())):
    command = list(raw_input().split())
    if command[0]=="pop":q.pop()
    if command[0]=="popleft":q.popleft()
    if command[0]=="append":q.append(command[1])
    if command[0]=="appendleft":q.appendleft(command[1])
for x in q:
    print x,
print