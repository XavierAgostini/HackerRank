import numpy as np
import math
class KalmanFilter(object):
	q = np.float32(0.0)
	r = np.float32(0.0)
	x = np.float32(0.0)
	p = np.float32(0.0)
	k = np.float32(0.0)

	def __init__(self, q, r, p=np.float32(0.0), k=np.float32(0.0), initial_value=np.float32(0.0)):
		self.q = q
		self.r = r
		self.p = p
		self.x = initial_value

	def update(self, measurement):
		self.p = np.float32(self.p +self.q)
		self.k = np.float32(self.p / (self.p + self.r))
		self.x = np.float32(self.x + self.k * (measurement - self.x))
		self.p = np.float32((1-self.k)* self.p)

		#return "p: " +str(self.p) + ", k: " +str(self.k) + ", output x: "+ str(self.x)
		return self.x
kalman1 = KalmanFilter(q=0.1, r=0.1);

inputArray =np.array([0.1,0.1,0.2,0.3,0.4], dtype='float32')
outputArray =np.array([0.0,0.0,0.0,0.0,0.0], dtype='float32')
diffArray =np.array([0.0,0.0,0.0,0.0,0.0], dtype='float32')

#Get output array
for i in range(0,5):	
	outputArray[i]=kalman1.update(inputArray[i])
print "outputArray: " , outputArray

avg=0
#get diffArray
for i in range(0,5):	
	diffArray[i]=outputArray[i]-inputArray[i]
	avg+=diffArray[i]
print "diffArray: ",diffArray

#get mean of diffArray
avg = avg/5
print "mean diff: ", avg


#get standard deviation
# stanDev=0
# for i in range(0,5):
# 	stanDev+= pow((diffArray[i] - avg),2)
# stanDev= pow(((1/5)*stanDev),0.5)
# print "stanDev1: ",stanDev
print "stanDev2: ",np.std(diffArray)

#get correlation

print "np_corr: ", np.correlate(inputArray,outputArray,'full')
#corrArr=[0,0,0,0,0]
corrArr = []
tempSum = np.float32(0.0)
arrLength = 5
tempLength = 2*arrLength-1 #2*4-1=7
for i in range(0,tempLength):
	for k in range(0,tempLength):
		if i < tempLength/2:
			if k <= i:
				tempSum+=inputArray[k]*outputArray[tempLength/2+ k -i]
		else:
			#tempLength = tempLength/2+1
			if k <=tempLength/2 and tempLength/2 + k - i >=0:
				#tempLength+=1
				tempSum+=inputArray[k]*outputArray[tempLength/2 + k - i]
			#do more shit
	# print "i: ",i	
	corrArr.append(tempSum)
	tempSum=0.0
print "my_corr: ", corrArr

#get convolutiuon 
tempSum = np.float32(0.0)
print "convolution ", np.convolve(outputArray,inputArray) 
convolArr =np.array([0.0,0.0,0.0,0.0,0.0], dtype='float32')
for i in range(0,5):	
	for k in range(0,5):
		tempSum += inputArray[k]*outputArray[i-k]
		# print "test: ",tempSum
	# print "______"
	convolArr[i]= tempSum
	tempSum = np.float32(0.0)
#print "convolArr: ", convolArr

