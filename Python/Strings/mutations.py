s = raw_input()
command = raw_input().split()
index = int(command[0])
letter = command[1]
s = s[:index]+letter+s[index+1:]
print s
