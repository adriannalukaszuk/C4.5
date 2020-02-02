from id3 import ID3
from c45 import C45
from Data import Data
from Validation import Validation

if __name__ == "__main__":
    d1 = Data('spliceATrainKIS.dat')
    d2 = Data('spliceDTrainKIS.dat')
    c1 = ID3(d2)
    tree = c1.generateTree()
    c1.evaluate()
    c2 = C45(d2)
    c2.adjustWithC45(tree)
    c2.evaluateC45Tree()

    d2.fetchData()
    v = Validation(d2)
    v.split_to_train_test(1)
