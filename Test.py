"""
@file Test.py
@author Marcin Kretkowski, Adrianna Łukaszuk
"""

import datetime
from id3 import ID3
from c45 import C45
from Data import Data
from Validation import Validation

class Test:

    @staticmethod
    def save_to_file(k, time, id3, c45):
            name = str(time).replace(':', '_')
            with open(f'{k}-{name}.txt', 'a') as file:
                file.write(f'{round(id3, 2)}    {round(c45, 2)}\n')

    @staticmethod
    def performTest(dataService, k):
        dataService.fetchData()
        v = Validation(dataService, k)
        errorID3 = []
        errorC45 = []
        time = datetime.datetime.now().time()
        for i in range(k):
            print(f'Iteration: {i}, error rate:')
            train, test = v.split_to_train_test(i)
            id3_algorithm = ID3(train, dataService.attrValues, dataService.classes)
            tree = id3_algorithm.generateTree()
            errorID3.append(id3_algorithm.evaluate(test))
            c45_algorithm = C45(train, dataService.attrValues, dataService.classes)
            c45_algorithm.adjustWithC45(tree)
            errorC45.append(c45_algorithm.evaluateC45Tree(test))
            Test.save_to_file(k, time, errorID3[i], errorC45[i])
        
        MeanErrorID3 = round(100 * sum(errorID3)/k, 2)
        MeanErrorC45 = round(100 * sum(errorC45)/k, 2)

        Test.save_to_file(k, time, MeanErrorID3, MeanErrorC45)
        Test.save_to_file(k, time, len(train), (len(train)/len(v.data))*100)

        print(f'ID3 mean error: {MeanErrorID3}%')
        print(f'C45 mean error: {MeanErrorC45}%')

    