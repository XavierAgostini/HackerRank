s = raw_input()
stuart = 0
kevin = 0
for i, char in enumerate(s):
    if char in "AEIOU":
        kevin+=len(s)-i
    else:
        stuart+=len(s)-i
if stuart > kevin: print "Stuart %s" %stuart
elif kevin > stuart: print "Kevin %s" %kevin
else: print "Draw"