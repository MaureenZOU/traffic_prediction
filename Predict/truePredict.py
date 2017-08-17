import numpy
from random import uniform
import sys
import csv
import os

def readData(fileName):
    with open(fileName) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        dataSet = []
        for row in spamreader:
            entry = []
            for data in row:
                entry.append(float(data))
            dataSet.append(numpy.array(entry))

    return numpy.array(dataSet)

def getDataMatrix(fileName):
    with open(fileName) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        dataSet = []
        for row in spamreader:
            entry = []
            for data in row:
                entry.append(data)
            dataSet.append(entry)

    return dataSet

def getPredictBatch(dataSet, NodeInfo, busyRatio, look_back):
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

            batchX.append(busyRatio[int(line[j]) - 1][1])
            trainBatch.append(batchX)

    return trainBatch, Y

def writeFile(fileName, Matrix):
    with open(fileName, 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in Matrix:
            spamwriter.writerow(row)

#######Predicting the full time slot for the data########
for num in range(0, 24):
    look_back = 4
    fileName = './feed/num_adjNodeList_levelNum_3.csv'
    NodeInfo = getDataMatrix(fileName)
    fileName = './feed/busyRatio.csv'
    busyRatio = getDataMatrix(fileName)
    fileName = './feed/predictRaw.csv'
    dataSet = getDataMatrix(fileName)

    predictX, Y= getPredictBatch(dataSet, NodeInfo, busyRatio, look_back)

    Xname = 'predict0406X.csv'
    writeFile(Xname, predictX)

    os.system('sh train.sh')

    fileName = './benchmark/num_adjNodeList_levelNum_3.csv'
    NodeInfo = readData(fileName)
    fileName = './result/result.csv'
    predict = readData(fileName)

    lastNodeInfo = NodeInfo[:,3]
    lastNodeInfo = lastNodeInfo.astype(int)
    predict = numpy.reshape(predict, (len(predict)))
    lastNodeSet = set(lastNodeInfo)

    resultList = [[] for i in range(0, len(lastNodeSet))]

    for i in range(0, len(lastNodeInfo)):
        resultList[int(lastNodeInfo[i])-1].append(int(predict[i]))

    predictY = []
    for resultSet in resultList:
        resultSet = numpy.array(resultSet)
        predictY.append(numpy.average(resultSet))

    predictY = numpy.reshape(predictY, (len(predictY), 1))

    fileName = 'realPredict.csv'
    ori_predictY = readData(fileName)
    if len(ori_predictY) == 0:
        new_predictY = numpy.around(predictY)
    else:
        new_predictY = numpy.c_[ori_predictY, numpy.around(predictY)]

    writeFile(fileName, new_predictY)

    predictY = numpy.reshape(predictY, (len(predictY)))
    predictY = numpy.append([201600000000], predictY)
    predictY = numpy.reshape(predictY, (len(predictY), 1))
    predictY = predictY.astype('int')

    dataSet = numpy.array(dataSet)
    new_predictX = numpy.c_[dataSet[:,[0,1]], dataSet[:,[2,look_back]], predictY]
    print(new_predictX.shape)
    fileName = './feed/predictRaw.csv'
    writeFile(fileName, new_predictX.tolist())




