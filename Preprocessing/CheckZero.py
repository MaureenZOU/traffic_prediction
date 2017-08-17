from datetime import date
import csv


def getLabel():
    with open('speeds_final.csv') as csvfile:
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
    #The label is the dictionary of timeslot
    return label

def getDataMatrix():
    with open('speeds_final.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        dataSet = []
        for i, row in enumerate(spamreader):
            if i!=0:
                entry = []
                for j, data in enumerate(row):
                    #数据比Label多一个
                    if j != 0 and j != len(row) - 1:
                        entry.append(int(data))
                dataSet.append(entry)

    return dataSet

def checkConsecutive(dataSet, label):
    problemDate = set()
    for i, row in enumerate(dataSet):
        count = 0
        for j, data in enumerate(row):
            if data == 0:
                print("REPORT!")
    return problemDate



label=getLabel()
dataSet=getDataMatrix()
problemDate = checkConsecutive(dataSet, label)
problemDate = sorted(problemDate)
print("Done Preprocessing...")


