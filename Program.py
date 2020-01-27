from c45 import C45

if __name__ == "__main__":
    c1 = C45("spliceATrainKIS.dat")
    c1.fetchData()
    c1.generateTree()
    c1.printTree()