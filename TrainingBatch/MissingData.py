import csv


def getDataMatrix():
    with open('rawPredict_final.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        dataSet = []
        for row in spamreader:
            entry = []
            for data in row:
                entry.append(data)
            dataSet.append(entry)

    return dataSet


def cleanZero(dataSet):
    i = 0
    for row in dataSet:
        j = 0
        for data in row:
            if i != 0 and j != 0 and data == '0':
                if j == 1:
                    row[j] = 1
                else:
                    row[j] = row[j - 1]
            j = j + 1
        i = i + 1

    return dataSet


def writeFile(dataSet):
    with open('mrawPredict_final.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in dataSet:
            spamwriter.writerow(row)


dataSet = getDataMatrix()
dataSet = cleanZero(dataSet)
writeFile(dataSet)
