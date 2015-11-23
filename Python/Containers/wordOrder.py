n=int(raw_input())
words = []
occurances = {}
for i in range(0,n):
    word = raw_input()
    if word not in occurances:
        words.append(word)
        occurances[word]=1
    else:
        occurances[word]+=1
print len(words)
for word in words:
    print occurances[word],
print