from sklearn.model_selection import train_test_split

class Data:
    def __init__(self):
        self.path_to_data = ''
        self.data = []
        self.classes = [0, 1]
        self.numAttributes = -1
        self.attrValues = ['C', 'T', 'G', 'A']
        self.attributes = []

    def fetchData(self, path_to_data):
        with open(path_to_data, 'r') as file:
            data = file.read().splitlines()
            self.numAttributes = len(data[2])
            self.attributes = range(self.numAttributes)
            for i in range(len(data)):
                if data[i] == '1':
                    self.data.append(f'{data[i+1]}1')
                elif data[i] == '0':
                    self.data.append(f'{data[i+1]}0')
    
    def split_to_train_test(self):
        train, test = train_test_split(self.data, test_size=0.33)
        #print(len(self.data), len(train), len(test))
        return train, test

a = Data()
a.fetchData('spliceDTrainKIS.dat')
a.split_to_train_test()