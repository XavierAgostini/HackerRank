N = int(raw_input())
classList = []
worstStudents = []
gradeA = []
gradeB = []
for i in range(0,N):
    name = raw_input()
    grade = float(raw_input())
    classList.append([name,grade])
    gradeA.append(grade)
    
worstMark = min(gradeA)
for x in gradeA:
    if x!=worstMark:
        gradeB.append(x)
nextLowest = min(gradeB)

for student in classList:
    if student[1]== nextLowest:
        worstStudents.append(student[0])
worstStudents = sorted(worstStudents)
for student in worstStudents:
    print student