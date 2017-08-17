import csv


def getLabel():
    with open('speed_delete_weekend_final.csv') as csvfile:
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


def getCut(label, startl, endl):
    #Don't forget to change the label here!!!!! 前两个是替换的时间段，后两个是被替换的时间段。
    for i in range(0, len(label)):
        if label[i] == startl:
            start = i
        if label[i] == endl:
            end = i

    return [start+1, end+2]


def getDataMatrix():
    with open('speed_delete_weekend_final.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        dataSet = []
        for row in spamreader:
            entry = []
            for data in row:
                entry.append(data)
            dataSet.append(entry)

    return dataSet


def changeMatrix(dataSet, start, end):
    for i in range(0, len(dataSet)):
            dataSet[i] = dataSet[i][0: start] + dataSet[i][end: len(dataSet[i])]
    return dataSet


def writeFile(dataSet):
    with open('speed_delete_weekend_weekday_final.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in dataSet:
            spamwriter.writerow(row)


label = getLabel()
dataSet = getDataMatrix()
pair = ['201605020000','201605132355']

start, end = getCut(label, pair[0], pair[1])
print("start: "+str(start))
print("end: "+str(end))
dataSet = changeMatrix(dataSet, start, end)

writeFile(dataSet)
