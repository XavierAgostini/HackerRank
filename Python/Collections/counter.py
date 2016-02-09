# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

x = int(raw_input())
shoeSizes = map(int, raw_input().split())
N = int(raw_input())
shoeCount = Counter(shoeSizes)
#print shoeCount
revenue = 0
for i in range(0,N):
    shoeSize,price = map(int, raw_input().split())
    if shoeCount[shoeSize]>0 :
        shoeCount[shoeSize]-=1
        revenue += price
    #print "shoeSize: " + str(shoeSize) + ", price: " + str(price)
print revenue 