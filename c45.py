class c45:
    
    def __init__(self, path_to_data):
        self.path_to_data = path_to_data
        self.data = []
        self.classes = [0, 1]
        self.numAttributes = -1
        self.attrValues = ['C', 'T', 'G', 'A']
        self.attributes = []

    def fetchData(self):
        with open(self.path_to_data, 'r') as file:
            data = file.read().splitlines()
            self.numAttributes = len(data[2])
            self.attributes = range(self.numAttributes)
            for i in range(len(data)):
                if data[i] == '1':
                    self.data.append(f'{data[i+1]}1')
                elif data[i] == '0':
                    self.data.append(f'{data[i+1]}0')
        
                




