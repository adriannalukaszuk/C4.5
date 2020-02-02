from Node import Node
from Data import Data

class C45:
    def __init__(self, data):
        self.test, self.data = data.split_to_train_test()
        self.classes = [0, 1]
        self.numAttributes = len(self.data[0])-1
        self.attrValues = data.attrValues

    def adjustWithC45(self, tree):
        self.tree = self.depthAdjustment(tree, self.data)

    def depthAdjustment(self, subTree, data):
        for i in range(len(subTree.children)):
            if subTree.children[i].isLeaf == True:
                break
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
        if commonClassError >= subTreeError:
            node.isLeaf = True
            node.attribute = commonClass

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
        commonClass = list(self.classes).index(classFreq)

        return commonClass, error

    def getDataOnCondition(self, data, attribute, attributeValue):
        output = []
        i = 0
        for i in range(len(data)):
            if data[i][attribute] == self.attrValues[attributeValue]:
                output.append(data[i])

        return output

    def evaluateC45Tree(self):
        e = 0
        percent = 0
        dataLen = len(self.data)
        for data in self.data:
            curNode = self.tree
            while not curNode.isLeaf:
                for child in curNode.children:
                    if data[curNode.attribute] == self.attrValues[child.attributeValue]:
                        curNode = child
                        break

            percent += 1
            #print(f'{percent*100/dataLen}%')
            if data[-1] != str(curNode.attribute):
                e += 1

        error = e/dataLen
        print(error)