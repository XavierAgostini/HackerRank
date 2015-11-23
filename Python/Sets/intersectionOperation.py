A = int(raw_input())
french = set(map(int,raw_input().split()))
B = int(raw_input())
english = set(map(int,raw_input().split()))

print len(french.intersection(english))