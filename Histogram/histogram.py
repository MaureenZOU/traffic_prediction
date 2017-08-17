import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pandas

fileName = './data/speeds.csv'
dataframe = pandas.read_csv(fileName, header = 1, index_col = 0, engine='python')
dataset = dataframe.values
dataSet = dataset.astype('int32')
print(dataSet)

dataSet=list(dataSet)
list=[]

def displayWithZero(dataSet):

	numList = [0 for i in range(0,5)]
	for line in dataSet:
		for data in line:
			numList[data] = numList[data] + 1

	print(numList)
	for line in dataSet:
	    for data in line:
	    	list.append(data)
	return list


def displayWithNonZero(dataSet):


	for line in dataSet:
	    for data in line:
	    	if data != 0:
	    		list.append(data)
	return list

#Input file is speeds.csv, the file would display the number of 1,2,3,4 in the file, finally, display it in the histogram
#change displayZero = True -> Display Zero otherwise.
displayZero = True

if displayZero == True:
	list = displayWithZero(dataSet)
	plt.hist(list, 5, normed=1, facecolor='green', alpha=0.75)
	plt.show()
else:
	list = displayWithNonZero(dataSet)
	plt.hist(list, 4, normed=1, facecolor='green', alpha=0.75)
	plt.show()


# print(list)
#np.savetxt(sys.argv[1], list, delimiter=",")
        