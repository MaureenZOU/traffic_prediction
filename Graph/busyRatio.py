from datetime import datetime, date, time
import csv
import numpy
import json


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


# it returns all the labels for every time stamp 
def getDateLabel(dataMaitrix):
    label = []
    for i in range(1, len(dataMaitrix[0])):
        label.append(dataMaitrix[0][i])

    return label


def getDateDict(label):
    dateObject = {}
    for i in range(0, len(label)):
        day = label[i]
        day = list(day)
        year = int(''.join(day[0:4]))
        if day[4] == '0':
            month = int(day[5])
        else:
            month = int(''.join(day[4:6]))

        if day[6] == '0':
            cday = int(day[7])
        else:
            cday = int(''.join(day[6:8]))

        currentDate = date(year, month, cday)

        if day[8] == '0':
            hour = int(day[9])
        else:
            hour = int(''.join(day[8:10]))

        if day[10] == '0':
            min = int(day[11])
        else:
            min = int(''.join(day[10:12]))

        currentTime = time(hour, min)
        dateObject[i] = datetime.combine(currentDate, currentTime)

    return dateObject


def getRecordLoc(dateDict):
    recordList = []
    for i in range(0, len(dateDict)):
        if dateDict[i].hour >= 8 and dateDict[i].hour <= 10:
            recordList.append(i + 1)

    recordSet = set(recordList)

    return recordSet


def getRecordMatrix(dataMatrix, recordSet):
    outMatrix = []
    for i in range(1, len(dataMatrix)):
        newLine = []
        newLine.append(dataMatrix[i][0])
        for j in range(1, len(dataMatrix[i])):
            if j in recordSet:
                newLine.append(dataMatrix[i][j])
        outMatrix.append(newLine)

    return outMatrix


def getCalculateMatrix(outMatrix):
    finalMatrix = []
    for line in outMatrix:
        newLine = []
        for i in range(1, len(line)):
            newLine.append((int(line[i])))
        finalMatrix.append(newLine)

    finalMatrix = numpy.array(finalMatrix)

    return finalMatrix


def getWriteList(outMatrix, sumMatrix, length):
    writeMatrix = []
    for i in range(0, len(sumMatrix)):
        writeMatrix.append([outMatrix[i][0], sumMatrix[i] / length * 1.0 ])

    return writeMatrix

def getBusyDict(writeMatrix):
    busyDict = {}
    for line in writeMatrix:
        label = line[0]
        busyDict[label] = str(line[1])
    return busyDict

def writeMatrix(matrix):
    with open('./result/busy_ratio_final.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for row in matrix:
            spamwriter.writerow(row)   

# def writeJson(writeMatrix, fileName):
#     with open(fileName, 'w') as fp:
#         json.dump(writeMatrix, fp)


fileName = "train_0525_final.csv"
dataMatrix = getDataMatrix(fileName)
dateLabel = getDateLabel(dataMatrix)
dateDict = getDateDict(dateLabel)
recordSet = getRecordLoc(dateDict)
length = len(recordSet)
recordSet.add(0)
outMatrix = getRecordMatrix(dataMatrix, recordSet)
outMatrix = numpy.array(outMatrix)
finalMatrix = getCalculateMatrix(outMatrix)
sumMatrix = numpy.sum(finalMatrix, axis=1)
matrix = getWriteList(outMatrix, sumMatrix, length)
writeMatrix(matrix)


# busyDict = getBusyDict(writeMatrix)
# fileName = 'result/busyDict_str.json'
# writeFile(busyDict, fileName)