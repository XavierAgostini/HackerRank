# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(raw_input())
#x = ','.join(raw_input().split())
#print x

Student = namedtuple('Student', ','.join(raw_input().split()))
avg = 0.0
for i in range(0,n):
    row = raw_input().split()
    tempStud = Student(row[0],row[1],row[2],row[3])
    avg += float(tempStud.MARKS)
print avg/n