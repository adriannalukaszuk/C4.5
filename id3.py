"""
@file id3.py
@author Marcin Kretkowski, Adrianna Łukaszuk
"""
import math
from Node import Node
from Data import Data

class ID3:
    def __init__(self, data, attrValues, classes):
        self.data = data
        self.classes = classes
        self.attrValues = attrValues
        self.attributes = list(range(len(self.data[0]) - 1))
        self.tree = None

    def generateTree(self):
        self.tree = self.recursiveGenerateTree(self.data, self.attributes, '')

        return self.tree

    def recursiveGenerateTree(self, curData, curAttributes, attrValue):
        if len(curData) == 0:
            return Node(True, "Fail", attrValue)

        oneClass = ID3.sameClass(curData)
        if oneClass is not False:
            return Node(True, oneClass, attrValue)
        elif len(curAttributes) == 0:
            majority = self.getHighestFreqClass(curData)
            return Node(True, majority, attrValue)
        else:
            (best,splitted) = self.splitAttribute(curData, curAttributes)
            remainingAttributes = curAttributes[:]
            remainingAttributes.remove(best)
            node = Node(False, best, attrValue)
            node.children = [self.recursiveGenerateTree(splitted[i], remainingAttributes, self.attrValues[i]) for i in range(len(splitted))]
            return node

    def gain(self, unionSet, subsets):
        S = len(unionSet)
        impurityBeforeSplit = self.entropy(unionSet)
        weights = [len(subset)/S for subset in subsets]
        impurityAfterSplit = 0
        for i in range(len(weights)):
            impurityAfterSplit += weights[i]*self.entropy(subsets[i])
        totalGain = impurityBeforeSplit - impurityAfterSplit
        
        return totalGain
        
    def splitAttribute(self, curData, curAttributes):
        splitted = []
        maxEntropy = -1 * float("inf")
        best_attribute = -1
        for attribute in curAttributes:
            subsets = [[] for a in self.attrValues]
            for row in curData:
                for i in range(len(self.attrValues)):
                    if row[attribute] == self.attrValues[i]:
                        subsets[i].append(row)
                        break
            ent = self.gain(curData, subsets)
            if ent > maxEntropy:
                maxEntropy = ent
                splitted = subsets
                best_attribute = attribute

        return (best_attribute,splitted)

    def entropy(self, dataSet):
        size = len(dataSet)
        if size == 0:
            return 0
        
        classes = [0 for i in self.classes]
        for row in dataSet:
            classIndex = list(self.classes).index(int(row[-1]))
            classes[classIndex] += 1

        classes = (int(x)/size for x in self.classes)
        sum = 0
        for data in classes:
            sum += data * ID3.log(data)

        return sum*-1

    def getHighestFreqClass(self, curData):
        freq = [0]*len(self.classes)
        for row in curData:
            index = self.classes.index(int(row[-1]))
            freq[index] += 1
            
        maxInd = freq.index(max(freq))
        return self.classes[maxInd]

    @staticmethod
    def log(value):
        if(value == 0):
            return 0
        
        return math.log(value, 2)

    @staticmethod
    def sameClass(data):
        if len(data) == 0:
            return False
        for row in data:
            if row[-1] != data[0][-1]:
                return False

        return int(data[0][-1])

    def evaluate(self, testData):
        e = 0
        dataLen = len(testData)
        for data in testData:
            curNode = self.tree
            while not curNode.isLeaf:
                for child in curNode.children:
                    if data[curNode.attribute] == child.attributeValue:
                        curNode = child
                        break

            if data[-1] != str(curNode.attribute):
                e += 1

        error = e/dataLen
        print(f'ID3: {round(error * 100, 2)}%')

        return error

