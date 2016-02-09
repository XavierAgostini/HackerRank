# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
s = sorted(Counter(raw_input()).items(), key= lambda x: (-x[1],x[0]))[:3]
print("\n".join(x[0]+" "+str(x[1]) for x in s))