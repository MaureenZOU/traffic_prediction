import numpy
import pandas
from sklearn.metrics import mean_squared_error

def readData(fileName):
    dataframe = pandas.read_csv(fileName,
                                engine='python', header=None)
    dataset = dataframe.values
    dataSet = dataset.astype('float32')

    return dataSet

        
#get testMatrix
fileName = './benchmark/predict0406Y.csv'
testMatrix = readData(fileName)

#get predictMatrix
fileName = './result/result.csv'
tY = readData(fileName)

tY = numpy.array(tY)
dMatrix = testMatrix - tY

print(dMatrix)

num = numpy.count_nonzero(dMatrix)

error = mean_squared_error(testMatrix, tY)
error=error**(0.5)
print('mean_square_error:' +str(error))

accuracy = (len(dMatrix)*len(dMatrix[0])-num)/(len(dMatrix)*len(dMatrix[0])*1.0)
print('accuracy: '+str(accuracy))
    