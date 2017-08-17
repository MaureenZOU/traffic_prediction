import csv

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


def getTrainBatch(dataSet, NodeInfo, busyRatio, look_back):
    trainBatch = []
    Y = []
    for i in range(1, len(dataSet[0]) - look_back):
        for line in NodeInfo:
            batchX = []
            for j in range(0, len(line)):
                if j < len(line) - 1:
                    batchX.append(dataSet[int(line[j])][i + j])
                else:
                    Y.append(dataSet[int(line[j])][i + j])
            batchX.append(busyRatio[int(line[j]) - 1][1])
            trainBatch.append(batchX)

    return trainBatch, Y


def writeFile(writeMatrix, fileName):
    with open(fileName, 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in writeMatrix:
            spamwriter.writerow(row)


look_back = 4
fileName = './feed/num_adjNodeList_levelNum_3_final.csv'
NodeInfo = getDataMatrix(fileName)
fileName = './feed/busy_ratio_final.csv'
busyRatio = getDataMatrix(fileName)

trainX = []
trainY = []
for i in range(0, 11):
    fileName = './timeSlot7-10/' + str(i) + '.csv'
    dataSet = getDataMatrix(fileName)
    X, Y = getTrainBatch(dataSet, NodeInfo, busyRatio, look_back)
    trainX = trainX + X
    trainY = trainY + Y

Xname = './batch/trainX0525_7-10_final.csv'
Yname = './batch/trainY0525_7-10_final.csv'

writeFile(trainX, Xname)
writeFile(trainY, Yname)
