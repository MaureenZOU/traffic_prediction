import collections
import matplotlib.pyplot as plt
import networkx as nx
import csv
import sys
import copy
import collections
import itertools
import matplotlib
import matplotlib.cm as cm


def breadth_first_search(graph, root):
    queue = collections.deque([root])
    root = queue.popleft()
    breadth_first(graph, queue, root, 0)


def breadth_first(graph, queue, vertex, count):
    neighbourSet = set()
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            visited.add(neighbour)
            graphDepthDict[neighbour] = count
            neighbourSet.add(neighbour)
        else:
            if count < graphDepthDict[neighbour]:
                visited.add(neighbour)
                graphDepthDict[neighbour] = count
                neighbourSet.add(neighbour)

    neighbourSet = sorted(neighbourSet)

    for neighbour in neighbourSet:
        queue.append(neighbour)
        graphList[count].append(neighbour)
        vertex = queue.popleft()
        breadth_first(graph, queue, vertex, count + 1)


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
    NodeList = []
    for i in range(1, len(dataMatrix)):
        NodeList.append(dataMatrix[i][0])

    return NodeList


def getNodeData():
    graph = []
    with open('graph_final.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            line = []
            for data in row:
                line.append(data)
            graph.append(line)

    return graph


def getGraph(topo):
    graph = {}

    graphInfo = set()  # the node appear in graph file

    for line in topo:
        graphInfo.add(line[0])

    for data in graphInfo:
        graph[data] = set()

    # create the graph from graph file
    for line in topo:
        graph[line[0]].add(line[1])

    for data in graphInfo:
        graph[data] = list(graph[data])

    return graph, graphInfo


def writeFile(writeMatrix, fileName):
    with open(fileName, 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in writeMatrix:
            spamwriter.writerow(row)


fileName = 'train_0525_final.csv'
dataMatrix = getDataMatrix(fileName)
NodeList = getNodeLabel(dataMatrix)
NodeSet = set(NodeList)
levelNum = 3

WriteList = []

outName = "./result/adjNodeList_levelNum_" + str(levelNum) + "_final.csv"

for baseNode in NodeList:
    visited = set()
    graphList = [[] for i in range(0, 330)]
    graphDepthDict = {}

    # Initial the basic information for the graph
    visited.add(baseNode)
    graphDepthDict[baseNode] = -1

    graphFileData = getNodeData()
    graph, graphInfo = getGraph(graphFileData)

    fullGraph = copy.deepcopy(graph)

    # create the mapping for the node without neighbour
    for fullLabel in NodeSet:
        if fullLabel not in graphInfo:
            fullGraph[fullLabel] = [fullLabel]

    breadth_first_search(fullGraph, baseNode)

    PartitionList = []
    PartitionList.append([baseNode])

    for i in range(0, levelNum):
        PartitionList.append(graphList[i])

    occurFlag = False

    for element in itertools.product(*PartitionList):
        WriteList.append(list(element))
        occurFlag = True

    if occurFlag == False:
        WriteList.append([baseNode for i in range(0, levelNum + 1)])

writeFile(WriteList, outName)
