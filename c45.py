import math
from node import Node

class C45:
    def __init__(self, path_to_data):
        self.path_to_data = path_to_data
        self.data = []
        self.classes = ['0', '1']
        self.numAttributes = -1
        self.attrValues = ['C', 'T', 'G', 'A']
        self.attributes = []

    def fetchData(self):
        with open(self.path_to_data, 'r') as file:
            data = file.read().splitlines()
            self.numAttributes = len(data[2])
            self.attributes = list(range(self.numAttributes))
            for i in range(len(data)):
                if data[i] == '1':
                    self.data.append(f'{data[i+1]}1')
                elif data[i] == '0':
                    self.data.append(f'{data[i+1]}0')

    def generateTree(self):
        self.tree = self.recursiveGenerateTree(self.data, self.attributes)

    def recursiveGenerateTree(self, curData, curAttributes):
        if len(curData) == 0:
            return Node(True, "Fail")

        oneClass = C45.sameClass(curData)
        if oneClass is not False:
            return Node(True, oneClass)
        elif len(curAttributes) == 0:
            majority = self.getHighestFreqClass(curData)
            return Node(True, majority)
        else:
            (best,splitted) = self.splitAttribute(curData, curAttributes)
            remainingAttributes = curAttributes[:]
            remainingAttributes.remove(best)
            node = Node(False, best)
            node.children = [self.recursiveGenerateTree(subset, remainingAttributes) for subset in splitted]
            return node

    def gain(self, unionSet, subsets):
        S = len(unionSet)
        impurityBeforeSplit = self.entropy(unionSet)
        weights = [len(subset)/S for subset in subsets]
        impurityAfterSplit = 0
        for i in range(len(subsets)):
            impurityAfterSplit += weights[i]*self.entropy(subsets[i])

        totalGain = impurityBeforeSplit - impurityAfterSplit
        
        return totalGain
        
    def splitAttribute(self, curData, curAttributes):
        splitted = []
        maxEntropy = -1 * float("inf")
        best_attribute = -1
        for attribute in curAttributes:
            valuesForAttribute = self.data[:][attribute]
            subsets = [[] for a in valuesForAttribute]
            for row in curData:
                for i in range(len(valuesForAttribute)):
                    if row[i] == valuesForAttribute[i]:
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
                
        prob_counter = [0 for i in self.classes]
        for row in dataSet:
            classIndex = list(self.classes).index(row[-1])
            prob_counter[classIndex] += 1

        prob_counter = (int(x)/size for x in self.classes)
       
        sum = 0
        for data in prob_counter:
            sum += data * C45.log(data)

        return sum*-1

    def getHighestFreqClass(self, curData):
        freq = [0]*len(self.classes)
        for row in curData:
            index = self.classes.index(row[-1])
            freq[index] += 1
            
        maxInd = freq.index(max(freq))
        return self.classes[maxInd]

    def printTree(self):
        self.printNode(self.tree)

    def printNode(self, node, indent=""):
        if not node.isLeaf:
			#discrete
            for index,child in enumerate(node.children):
                if child.isLeaf:
                    print(indent + node.label + " = " + self.attributes[index] + " : " + child.label)
                else:
                    print(indent + node.label + " = " + self.attributes[index] + " : ")
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