import numpy as np
# correlation = np.correlate(inputArray, outputArray, 'full')
#print 'correlation_np', correlation
g = [1.0,2.0,3.0,4.0]
h =[5.0,6.0,7.0,8.0]
print "test corr: ", np.correlate(g,h,'full')
#corrArr=[0,0,0,0,0]
corrArr = []
tempSum = np.float32(0.0)
arrLength = 4
tempLength = 2*arrLength-1 #2*4-1=7
for i in range(0,tempLength):
	for k in range(0,tempLength):
		if i < tempLength/2:
			if k <= i:
				tempSum+=g[k]*h[tempLength/2+ k -i]
		else:
			#tempLength = tempLength/2+1
			if k <=tempLength/2 and tempLength/2 + k - i >=0:
				#tempLength+=1
				tempSum+=g[k]*h[tempLength/2 + k - i]
			#do more shit
	# print "i: ",i	
	corrArr.append(tempSum)
	tempSum=0.0
print "my corr: ", corrArr