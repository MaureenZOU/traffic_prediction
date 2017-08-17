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

def getNodeLabel(dataMatrix):
    NodeDict = {}
    for i in range(1, len(dataMatrix)):
        NodeDict[dataMatrix[i][0]] = i

    return NodeDict

def changeLabel(NodeDict, NodeList):
    Matrix = []
    for line in NodeList:
        newLine = []
        for data in line:
            newLine.append(NodeDict[data])
        Matrix.append(newLine)
        
    Matrix = numpy.array(Matrix)
    print(Matrix)
    Matrix = numpy.fliplr(Matrix)
    print(Matrix)
    
    return Matrix
    
def writeFile(writeMatrix, fileName):
    
    with open(fileName, 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in writeMatrix:
            spamwriter.writerow(row)

fileName = 'train_0525_final.csv'
dataMatrix = getDataMatrix(fileName)
NodeDict = getNodeLabel(dataMatrix)

fileName = './result/adjNodeList_levelNum_3_final.csv'
NodeList = getDataMatrix(fileName)

changeMatrix = changeLabel(NodeDict, NodeList)

fileName = './result/num_adjNodeList_levelNum_3_final.csv'
writeFile(changeMatrix, fileName)








