"""
@file Validation.py
@author Marcin Kretkowski, Adrianna Łukaszuk
"""

import random

class Validation:

    def __init__(self, data, k=10):
        self.data = data.data
        random.shuffle(self.data)
        self.k = k
    
    def split_to_train_test(self, t):
        n = int(len(self.data)/self.k)
        data = [self.data[i:i+n] for i in range(0, len(self.data), n)]
        data[-2] += data.pop()
        test = data[t]
        train = []
        for i in range(self.k):
            if i != t:
                train += data[i]
                
        train1, train2 = train[0:int(len(train)/2)], train[int(len(train)/2):]

        return train1, train2, test
        
