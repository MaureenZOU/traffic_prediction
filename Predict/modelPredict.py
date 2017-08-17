import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense, LSTM, Activation, Dropout
from keras.models import load_model
from keras.models import model_from_json
from random import uniform
import sys
import keras
import json

def readData(fileName):
    dataframe = pandas.read_csv(fileName,
                                engine='python', header=None)
    dataset = dataframe.values
    dataSet = dataset.astype('float32')

    return dataSet

def getTrainBatch(dataSet, NodeInfo, busyRatio, look_back):
    trainBatch = []
    Y = []
    
    for i in range(1, 2):
        for line in NodeInfo:
            batchX = []
            for j in range(0, len(line)):
                if j < len(line) - 1:
                    batchX.append(dataSet[int(line[j])][i + j])
                else:
                    Y.append(dataSet[int(line[j])][i + j])

            batchX.append(busyRatio[int(line[j]) - 1][0])
            trainBatch.append(batchX)

    return trainBatch, Y
    
def cookData(matrix):
    matrix = numpy.reshape(matrix, (matrix.shape[0], 1, matrix.shape[1]))
    return matrix


def fitModel(trainX, trainY, model, epochs, batch_size):
    model.fit(trainX, trainY, nb_epoch=epochs, batch_size=batch_size, verbose=2)
    return model

def loadModel(fileName):
    print('Start loading model...')
    model = load_model(fileName)
    print('End loading model')
    return model
    
def predict(predictX):
    Y = []
    
    for line in predictX:
        line = numpy.reshape(line,(1,1,len(line[0])))
        Y.append(model.predict(line))

    return Y

def myround(valueList):
    for element in valueList:
        if element >= 3.5:
            return 4.0
        elif element >= 2.5:
            return 3.0
        elif element > 1.5:
            return 2.0
        else:
            return 1.0

def averageRound(valueList):
    avg = 0
    for element in valueList:
        avg = avg + element
    
    avg = avg / len(valueList)
    
    if avg >= 3.5:
        return 4.0
    elif avg >= 2.5:
        return 3.0
    elif avg > 1.5:
        return 2.0
    else:
        return 1.0

 
def getPredictBatch(dataSet, NodeInfo, busyRatio, look_back):
    trainBatch = []
    
    for line in NodeInfo:
        batchX = []
        for j in range(0, len(line)):
            if j < len(line) - 1:
                batchX.append(dataSet[int(line[j])-1][j])
            else:
                batchX.append(busyRatio[int(line[j]) - 1])
        trainBatch.append(batchX)

    return numpy.array(trainBatch)
  
def getPredictList(dataMatrix):
    print(dataMatrix[0][0])
    label = int(dataMatrix[0][0])
    predict = [[] for i in range(0, 328)]
    predict[label-1].append(dataMatrix[0][1])
    
    for line in dataMatrix:
        if line[0] != label:
            label = int(line[0])
            predict[label-1].append(line[1])
        else:
            predict[label-1].append(line[1])
            
    return predict


def writeOutput(fileName, Y):
    numpy.savetxt(fileName, Y, delimiter=",")

#######Predicting the full time slot for the data########
look_back = 4
fileName = './data/num_adjNodeList_3_delete1955.csv'
NodeInfo = readData(fileName)
fileName = './data/busyRatio_delete1955.csv'
busyRatio = readData(fileName)

#get the last node Info(1,2,3...)
NodeInfo = numpy.array(NodeInfo)
lastNodeInfo = NodeInfo[:,3]

#get the busy ratio base on node order
busyRatio = numpy.array(busyRatio) 
busyRatio = busyRatio[:,1]

##########You need to change the pretrained model Name########
#load pretrained model
fileName = './benchmark/model_test1_50000_700.h5'
model = loadModel(fileName)

#generate predict set
fileName = './data/predict0406Y.csv'
predictRawSet = readData(fileName)

#get testMatrix
fileName = './data/test_0406_delete1955.csv'
testMatrix = readData(fileName)

tY = None
for i in range(0, len(testMatrix[0])):
    print(str(i)+"th round!")
    predictX = getPredictBatch(predictRawSet, NodeInfo, busyRatio, look_back)
    predictX = cookData(predictX)
    #predict on predict batch
    Y = predict(predictX)
    
    Y = numpy.reshape(Y, (len(Y),1))
    #add the column of last node info and predict Y
    nodePredictMatrix = numpy.c_[lastNodeInfo, Y]

    #get the predict list from the matrix 
    predictList = getPredictList(nodePredictMatrix)
    
    #get the final result of the current time slot
    result = []
    
    for line in predictList:
        result.append(averageRound(line))
        
    result = numpy.reshape(result,(len(result),1))
    
    if i == 0:
        tY = result
    else:
        tY = numpy.c_[tY,result]
    
    predictRawSet = numpy.delete(predictRawSet, 0, 1)
    predictRawSet = numpy.c_[predictRawSet, result]
    
########You need to change this part fit different model Name########
fileName = './result/avgresult_50000_700.csv' 

writeOutput(fileName, tY)





