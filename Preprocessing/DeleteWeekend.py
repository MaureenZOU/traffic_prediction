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
    return label


def getDateObject(label):

    dateObject={}
    for i in range(0, len(label)):
        day = label[i]
        day = list(day)
        year = int(''.join(day[0:4]))
        if day[4] == '0':
            month = int(day[5])
        else:
            month = int(''.join(day[4:6]))

        if day[6]=='0':
            cday=int(day[7])
        else:
            cday=int(''.join(day[6:8]))

        currentDate=date(year,month,cday)
        dateObject[i]=currentDate

    return dateObject

def getWeekendTag(dateObjects):

    tag=set()
    for i in range(0,len(dateObjects)):
        if dateObjects[i].isoweekday()==6 or dateObjects[i].isoweekday()==7:
            tag.add(i)

    return tag

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

    with open('speed_delete_weekend_final.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in weekset:
            spamwriter.writerow(row)


label=getLabel()
dateObject=getDateObject(label)
tag=getWeekendTag(dateObject)
dataSet=getDataMatrix()
weekset=deleteWeekend(dataSet,tag)
writeTempFile(weekset)


