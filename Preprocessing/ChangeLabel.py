from datetime import date
import csv


def getLabel():
    with open('speed_delete_weekend_weekday.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        labelList = []

        for row in spamreader:
            labelList = row;
            break

    return labelList



def getDataMatrix():
    with open('speed_delete_weekend_weekday.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        dataSet = []
        for row in spamreader:
            entry = []
            for data in row:
                entry.append(data)
            dataSet.append(entry)

    return dataSet

def deleteWeekend(dataSet,tag):

    weekset=[]
    for row in dataSet:
        entry=[]
        entry.append(row[0])
        for i in range(0,len(row)):
            if i!=0 and ((i-1) not in tag):
                entry.append(row[i])
        weekset.append(entry)

    return weekset

def writeTempFile(weekset):

    with open('speed_delete_weekend_weekday.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in weekset:
            spamwriter.writerow(row)


labelList=getLabel()
dataSet=getDataMatrix()
dataSet[0] = labelList
writeTempFile(dataSet)


