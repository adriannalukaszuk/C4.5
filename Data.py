from sklearn.model_selection import train_test_split

class Data:
    def __init__(self, path_to_data):
        self.path_to_data = path_to_data
        self.data = []
        self.classes = [0, 1]
        self.numAttributes = -1
        self.attrValues = ['C', 'T', 'G', 'A']
        self.attributes = []
        self.tree = None

    def fetchData(self):
        with open(self.path_to_data, 'r') as file:
            data = file.read().splitlines()
            for i in range(len(data)):
                if data[i] == '1':
                    self.data.append(f'{data[i+1]}1')
                elif data[i] == '0':
                    self.data.append(f'{data[i+1]}0')
    
    def split_to_train_test(self):
        self.fetchData()
        train, test = train_test_split(self.data, test_size=0.33)
        return train, test
