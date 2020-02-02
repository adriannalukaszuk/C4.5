"""
@file c45.py
@author Marcin Kretkowski, Adrianna Łukaszuk
"""

from Node import Node
from Data import Data

class C45:
    def __init__(self, data, attrValues, classes):
        self.data = data
        self.classes = classes
        self.attrValues = attrValues

    def adjustWithC45(self, tree):
        self.tree = self.depthAdjustment(tree, self.data)

    def depthAdjustment(self, subTree, data):
        if len(data) == 0:
            return subTree

        for i in range(len(subTree.children)):
            if subTree.children[i].isLeaf == True:
                if subTree.children[i].attribute == 'Fail':
                    commonClass, _ = self.evaluateCommonClass(data)
                    subTree.children[i].attribute = commonClass
            else:
                subData = self.getDataOnCondition(data, subTree.attribute, subTree.children[i].attributeValue)
                evaluation = self.evaluate(subData, subTree.children[i])
                if evaluation is not False:
                    return evaluation

                subTree.children[i] = self.depthAdjustment(subTree.children[i], subData)
                
        return subTree

    def evaluate(self, data, node):
        commonClass, commonClassError = self.evaluateCommonClass(data)
        subTreeError = self.evaluateSubTree(data, node)
        if subTreeError >= commonClassError:
            #print(f'commonClassError: {commonClassError}, subTreeError: {subTreeError}')
            node.isLeaf = True
            node.attribute = commonClass
            node.children = []

            return node

        return False

    def evaluateSubTree(self, data, node):
        error = 0
        for row in data:
            curNode = node
            while not curNode.isLeaf:
                for child in curNode.children:
                    if row[curNode.attribute] == self.attrValues[child.attributeValue]:
                        curNode = child
                        break

            if row[-1] != str(curNode.attribute):
                error += 1

        return error

    def evaluateCommonClass(self, data):
        classes = [0 for i in self.classes]
        for row in data:
            classIndex = list(self.classes).index(int(row[-1]))
            classes[classIndex] += 1

        classFreq = max(classes)
        error = sum(classes) - classFreq
        commonClass = list(classes).index(classFreq)

        return commonClass, error

    def getDataOnCondition(self, data, attribute, attributeValue):
        output = []
        i = 0
        for i in range(len(data)):
            if data[i][attribute] == self.attrValues[attributeValue]:
                output.append(data[i])

        return output

    def evaluateC45Tree(self, testData):
        e = 0
        dataLen = len(testData)
        for data in testData:
            curNode = self.tree
            while not curNode.isLeaf:
                for child in curNode.children:
                    if data[curNode.attribute] == self.attrValues[child.attributeValue]:
                        curNode = child
                        break

            if data[-1] != str(curNode.attribute):
                e += 1

        error = e/dataLen
        print(f'C45: {error}')

        return error