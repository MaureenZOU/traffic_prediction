import csv


def getLabel():
    with open('speed_delete_weekend.csv') as csvfile:
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


def getCut(label, copy, paste):
    #Don't forget to change the label here!!!!! 前两个是替换的时间段，后两个是被替换的时间段。
    for i in range(0, len(label)):
        if label[i] == copy + '0000':
            start = i
        if label[i] == copy + '2355':
            end = i
        if label[i] == paste + '0000':
            startm = i
        if label[i] == paste + '2355':
            endm = i

    return [start, end, startm, endm]


def getDataMatrix():
    with open('speed_delete_weekend.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        dataSet = []
        for row in spamreader:
            entry = []
            for data in row:
                entry.append(data)
            dataSet.append(entry)

    return dataSet


def changeMatrix(dataSet, start, end, startm, endm):
    i = 0
    for row in dataSet:
        if i != 0:
            row[startm + 1:endm + 2] = row[start + 1:end + 2]
        i = i + 1
    return dataSet


def writeFile(dataSet):
    with open('speed_delete_weekend_weekday.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in dataSet:
            spamwriter.writerow(row)


label = getLabel()
dataSet = getDataMatrix()
dateList = [['20160328','20160404']]

for pair in dateList:
    list = getCut(label, pair[0], pair[1])
    dataSet = changeMatrix(dataSet, list[0], list[1], list[2], list[3])

writeFile(dataSet)
