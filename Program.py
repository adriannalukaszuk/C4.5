from c45 import C45
from Data import Data

if __name__ == "__main__":
    d1 = Data('spliceATrainKIS.dat')
    d2 = Data('spliceDTrainKIS.dat')
    c1 = C45(d1)
    c1.generateTree()
    c1.evaluate()