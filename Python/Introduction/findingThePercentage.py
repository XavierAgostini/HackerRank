from __future__ import division

n = float(raw_input())
students = {}
i=n
while i>0:
    student = (raw_input()).split()
    students[student[0]] = student[1:]
    i-=1
choice = raw_input()
ave = 0.00
for grade in students[choice]:
    ave+=float(grade)
ave = ave/len(students[choice])
print "{0:.2f}".format(ave)