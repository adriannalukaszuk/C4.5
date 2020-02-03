"""
@file Data.py
@author Marcin Kretkowski, Adrianna Łukaszuk
"""

class Data:
    def __init__(self, path_to_data):
        self.path_to_data = path_to_data
        self.data = []
        self.attrValues = []
        self.classes = [0, 1]

    def fetchData(self):
        self.data = []
        with open(self.path_to_data, 'r') as file:
            data = file.read().splitlines()
            for i in range(len(data)):
                if data[i] == '1':
                    self.data.append(f'{data[i+1]}1')
                elif data[i] == '0':
                    self.data.append(f'{data[i+1]}0')

            for data in self.data:
                for i in range(len(data)-1):
                    if data[i] not in self.attrValues:
                        self.attrValues.append(data[i])
    