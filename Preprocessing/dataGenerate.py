import csv
import sys

#Please Adjust the cutDate
cutDate = '0518'

def getLabel():
    with open('speeds_final.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        label = {}
        iteration = 0
        for row in spamreader:
            iterationj = 0
            for data in row:
                if iterationj != 0 and iteration == 0:
                    label[iterationj - 1] = int(data)
                iterationj = iterationj + 1

                # if iterationj!=0 and iteration!=0:
            break
    return label


def getDataMatrix():
    with open('speeds_final.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        dataSet = []
        for row in spamreader:
            entry = []
            for data in row:
                entry.append(data)
            dataSet.append(entry)

    return dataSet


def getCutLoc(label):
    startLoc = 0
    endLoc = 0
    for i in range(0, len(label)):
        if label[i] == int('2016'+cutDate+'0805'):
            startLoc = i
        if label[i] == int('2016'+cutDate+'1000'):
            endLoc = i

    return [startLoc, endLoc]


def generateTrainTest(dataSet, start, end):
    trainMatrix = []
    testMatrix = []

    for row in dataSet:
        trainEntry = []
        testEntry = []
        testEntry.append(row[0])
        for i in range(0, len(row)):
            if i < start + 1:
                trainEntry.append(row[i])
            elif i >= start + 1 and i <= end + 1:
                testEntry.append(row[i])
        testMatrix.append(testEntry)
        trainMatrix.append(trainEntry)

    return [testMatrix, trainMatrix]


def writeTrain(trainMatrix):
    with open('train_'+cutDate+'.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for row in trainMatrix:
            spamwriter.writerow(row)


def writeTest(testMatrix):
    with open('test_'+cutDate+'.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for row in testMatrix:
            spamwriter.writerow(row)

#This file is able to generate train and test data for a specific data, with command line argument for the MMDD
label = getLabel()
loc = getCutLoc(label)
print(loc)
dataSet = getDataMatrix()
writeSet = generateTrainTest(dataSet, loc[0], loc[1])
writeTrain(writeSet[1])
writeTest(writeSet[0])
