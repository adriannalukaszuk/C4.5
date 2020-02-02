from id3 import ID3
from c45 import C45
from Data import Data
from Validation import Validation

class Test:

    @staticmethod
    def performTest(dataService, k):
        dataService.fetchData()
        v = Validation(dataService, k)
        errorID3 = []
        errorC45 = []
        for i in range(k):
            print(f'Iteration: {i}, error rate:')
            train1, train2, test = v.split_to_train_test(i)
            id3_algorithm = ID3(train1, dataService.attrValues, dataService.classes)
            tree = id3_algorithm.generateTree()
            errorID3.append(id3_algorithm.evaluate(test))
            c45_algorithm = C45(train1 + train2, dataService.attrValues, dataService.classes)
            c45_algorithm.adjustWithC45(tree)
            errorC45.append(c45_algorithm.evaluateC45Tree(test))
        
        MeanErrorID3 = round(100 * sum(errorID3)/k, 2)
        MeanErrorC45 = round(100 * sum(errorC45)/k, 2)

        print(f'ID3 mean error: {MeanErrorID3}%')
        print(f'C45 mean error: {MeanErrorC45}%')
