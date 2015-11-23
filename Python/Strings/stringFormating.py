n = int(raw_input())
width = len('{0:b}'.format(n))
for i in range(1,n+1):
    for base in 'doXb':
        print "{0:{width}{base}}".format(i, base=base, width=width),
    print