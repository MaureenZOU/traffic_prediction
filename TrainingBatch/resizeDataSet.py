import csv
import random
import pandas
import numpy

def getDataMatrix(fileName):
    
    dataframe = pandas.read_csv(fileName,
                                engine='python', header=None)
    dataset = dataframe.values
    dataSet = dataset.astype('float32')

    return dataSet

def writeFile(writeMatrix, fileName):
    with open(fileName, 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in writeMatrix:
            spamwriter.writerow(row)

def randomDraw(trainX, trainY):
    finalX = []
    finalY = []
    
    for i in range(0, len(trainY)):
        
        if trainY[i] == 4.0:
            if random.uniform(0,1.0) < 1.0/10:
                finalX.append(trainX[i])
                finalY.append(trainY[i])
        
        if trainY[i] == 3.0:
            if random.uniform(0,1.0) < 1.0/10:
                finalX.append(trainX[i])
                finalY.append(trainY[i])
            
        if trainY[i] == 2.0:
            if random.uniform(0,1.0) < 1.0/10:
                finalX.append(trainX[i])
                finalY.append(trainY[i])
            

        if trainY[i] == 1.0:
            if random.uniform(0,1.0) < 1.0/10:
                finalX.append(trainX[i])
                finalY.append(trainY[i])
                
    return finalX, finalY
                        
XName = './batch/trainX0525_7-10_final.csv'
YName = './batch/trainY0525_7-10_final.csv'

trainX = getDataMatrix(XName)
trainY = getDataMatrix(YName)

trainY = numpy.reshape(trainY,(len(trainY)))

finalX, finalY = randomDraw(trainX, trainY)

XName = './batch/tmpX.csv'
YName = './batch/tmpY.csv'

finalY = numpy.reshape(finalY,(len(finalY),1))
print(len(finalY))

writeFile(finalX, XName)
writeFile(finalY, YName)
