import csv
from datetime import date
import numpy as np
import matplotlib.pyplot as plt
import sys


def getLabel():
    with open('speed_final(weekend,4.4,0).csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        label = {}
        iteration = 0
        for row in spamreader:
            iterationj = 0
            for data in row:
                if iterationj != 0 and iteration == 0:
                    label[iterationj - 1] = data
                iterationj = iterationj + 1

                # if iterationj!=0 and iteration!=0:
            break
    return label


def getDateObject(label):
    dateObject = {}
    time = {}
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

        time[i] = ''.join(day[8:12])
        currentDate = date(year, month, cday)
        dateObject[i] = currentDate

    return [dateObject, time]


def getDataMatrix():
    with open('speed_final(weekend,4.4,0).csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        dataSet = []

        i = 0
        for row in spamreader:
            entry = []
            j = 0
            for data in row:
                if i != 0 and j != 0 and j != 10465:
                    entry.append(float(data))
                j = j + 1
            if i != 0:
                dataSet.append(np.array(entry))
            i = i + 1

    return np.array(dataSet)


def changeMonday(dataSet, dataObject, time):
    for row in dataSet:
        for i in range(0, len(row)):
            if dataObject[i].isoweekday() == 1 and time[i] == '0000':
                print("hihihihi")
                row[i] = -3

    return dataSet


def getXY(dataSet, number):
    i = 0
    x = []
    y = []
    flag = False
    for row in dataSet:
        for j in range(0, len(row)):
            if i == number:
                flag = True
                x.append(row[j])
                y.append(j)
        if flag == True:
            break
        i = i + 1

    return [np.array(x), np.array(y)]


def plotData(x, y, node):
    plt.plot(x,y)

    plt.xlabel('time')
    plt.ylabel('congestion')
    plt.title('visualization of congestion overtime (-3 means split of every week)')
    plt.grid(True)
    plt.savefig("node"+str(node)+".png")
    plt.show()


###This is a python sript to viusalize data, with python argument 1-roadNum(0-329)
number = int(sys.argv[1])
label = getLabel()
list = getDateObject(label)
dateObject = list[0]
time = list[1]
dataSet = getDataMatrix()
#dataSet = changeMonday(dataSet, dateObject, time)
list = getXY(dataSet, number)
plotData(list[1], list[0],number)
