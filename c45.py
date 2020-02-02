import math
import random
from Node import Node
from Data import Data

class C45:
    def __init__(self, data):
        self.data = data.data
        self.classes = [0, 1]
        self.numAttributes = len(self.data[0])-1
        self.attrValues = data.attrValues
        self.attributes = list(range(self.numAttributes))
        self.tree = None

    def generateTree(self):
        self.tree = self.recursiveGenerateTree(self.data, self.attributes)

    def recursiveGenerateTree(self, curData, curAttributes, attrValue=[]):
        oneClass = C45.sameClass(curData)
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
            kids = []
            notClassified = []
            index = 0
            max = 0
            for i in range(len(splitted)):
                if len(splitted[i]) != 0:
                    if(len(splitted[i]) > max):
                        max = len(splitted[i])
                        index = len(kids)

                    kids.append(self.recursiveGenerateTree(splitted[i], remainingAttributes, i))
                else:
                    notClassified.append(i)

            if len(notClassified) != 0:
                for attrValue in notClassified:
                    kids[index].attributeValue.append(attrValue)

            node.children = kids
            
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

    #zalozenie: dataSet ma zbior elementow z takim samym argumentem warunkowym tj. np. P(decision| argument4 = 'G')
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
            sum += data * C45.log(data)

        return sum*-1

    def getHighestFreqClass(self, curData):
        freq = [0]*len(self.classes)
        for row in curData:
            index = self.classes.index(int(row[-1]))
            freq[index] += 1
            
        maxInd = freq.index(max(freq))
        return self.classes[maxInd]

    def printTree(self):
        self.printNode(self.tree)

    def printNode(self, node, indent=""):
        if not node.isLeaf:
			#discrete
            for child in node.children:
                if child.isLeaf:
                    print(indent + str(node.attribute) + " = " + str(child.attributeValue) + " : " + str(child.attribute))
                else:
                    print(indent + str(node.attribute) + " = " + str(child.attributeValue) + " : ")
                    self.printNode(child, indent + "	")

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


        return data[0][-1]

    def evaluate(self):
        e = 0
        precent = 0
        dataLen = len(self.test)
        for data in self.test:
            curNode = self.tree
            while not curNode.isLeaf:
                for child in curNode.children:
                    for attrValue in child.attributeValue:
                        if data[curNode.attribute] in self.attrValues[attrValue]:
                            curNode = child
                            break
                    
                    if curNode == child:
                        break

            precent += 1
            print(f'{precent*100/dataLen}%')

            if data[-1] != str(curNode.attribute):
                e += 1
        error = e/len(self.test)
        print(error)
            
         