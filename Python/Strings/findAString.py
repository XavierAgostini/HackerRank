string = raw_input()
substring = raw_input()
total=0
keepGoing = True
while keepGoing:
    index = string.find(substring)
    if index!=-1:
        total+=1
        string = string[index+len(substring)-1:]
    else:
        keepGoing = False
print total