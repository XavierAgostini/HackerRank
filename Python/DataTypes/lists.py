n = int(raw_input())
a = []
while n>0:
    command=raw_input().split()
    order = command[0]
    values = [int(element) for element in command[1:]]
    # print values
    if(order == "append"):
        for value in values:
            a.append(value)
    if(order == 'extend'):
        a.extend(values)
    if(order == 'insert'):
        a.insert(values[0],values[1])
    if(order == 'remove'):
        a.remove(values[0])
    if(order == 'pop' ):
        a.pop()
    if(order == 'index'):
        a.index(values[0])
    if(order == 'count'):
        a.count(values)
    if(order == 'sort'):
        a.sort()
    if(order == 'reverse'):
        a.reverse()
    if(order == 'print'):
        print a
        
    #print a
    n-=1
    b= False