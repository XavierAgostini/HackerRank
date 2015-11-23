K = int(raw_input())
roomList = map(int,raw_input().split())
roomSet = set(roomList)
sumList = sum(roomList)
#print sum(roomSet)*K
print (sum(roomSet)*K - sumList)/(K-1)