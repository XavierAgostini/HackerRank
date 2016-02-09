# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N = int(raw_input())
grocery_list = OrderedDict()

for i in range(0,N):
    item = raw_input().split()
    if len(item)>2: 
        item_name = ' '.join(item[0:len(item)-1])
    else:
        item_name = item[0]
    if item_name in grocery_list:
        grocery_list[item_name] += int(item[-1])
    else:
        grocery_list[item_name] = int(item[-1])

for item in grocery_list:
    print item + " " + str(grocery_list[item])
    
