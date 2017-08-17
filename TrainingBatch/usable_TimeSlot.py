from datetime import datetime, date, time
import csv
import numpy


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
        dateObject[i + 1] = datetime.combine(currentDate, currentTime)

    return dateObject


def getNodeLabel(dataMatrix):
    NodeList = ['id']
    for i in range(1, len(dataMatrix)):
        NodeList.append(dataMatrix[i][0])

    return NodeList


def preWrite(dataMatrix, dateObject, NodeLabel):
    count = 0
    dataMatrix = numpy.array(dataMatrix)

    curTime = dateObject[1].date()

    dayMatrix = numpy.array(NodeLabel)
    dayMatrix = numpy.reshape(dayMatrix, (len(NodeLabel), 1))

    for i in range(1, len(dataMatrix[0])):
        #########改时间段的时候Change这一行！！！！！！！！！
        if dateObject[i].date() == curTime and dateObject[i].time() > time(7, 0) and dateObject[i].time() < time(10,
                                                                                                                 00):
            dayMatrix = numpy.c_[dayMatrix, dataMatrix[:, i]]
        elif dateObject[i].date() != curTime:
            if dateObject[i].isoweekday() == 3:
                writeFile(curTime, dayMatrix, count)
                count = count + 1
            dayMatrix = numpy.array(NodeLabel)
            dayMatrix = numpy.reshape(dayMatrix, (len(NodeLabel), 1))
            curTime = dateObject[i].date()
            


def writeFile(curTime, dayMatrix, count):
    ###改时间段的时候要重新命名文件夹！！！！！！！
    fileName = './timeSlot7-10/' + str(count) + '.csv'

    with open(fileName, 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in dayMatrix:
            spamwriter.writerow(row)


fileName = "train_0525_final.csv"
dataMatrix = getDataMatrix(fileName)
label = getDateLabel(dataMatrix)
dateObject = getDateDict(label)
NodeLabel = getNodeLabel(dataMatrix)
preWrite(dataMatrix, dateObject, NodeLabel)
