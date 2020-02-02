from c45 import C45
from Data import Data
from Validation import Validation

if __name__ == "__main__":
    d1 = Data('spliceATrainKIS.dat')
    d2 = Data('spliceDTrainKIS.dat')
    d1.fetchData()
    
    v = Validation(d1)
    c1 = C45(d2)
    c1.generateTree()
    c1.evaluate()