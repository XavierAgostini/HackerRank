s = raw_input()
print True if any(i.isalnum() for i in s) else False
print True if any(i.isalpha() for i in s) else False
print True if any(i.isdigit() for i in s) else False
print True if any(i.islower() for i in s) else False
print True if any(i.isupper() for i in s) else False