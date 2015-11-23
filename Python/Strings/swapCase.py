S = raw_input()
newString =""
for i in range(0,len(S)):
    if S[i].isupper():
        newString+=S[i].lower()
    elif S[i].islower():
        newString+=S[i].upper()
    else:
        newString+=S[i]
print newString