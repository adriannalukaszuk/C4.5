from ID3 import ID3
from C45 import C45
from Data import Data
from Validation import Validation
from Test import Test

if __name__ == "__main__":
    d1 = Data('spliceATrainKIS.dat')
    d2 = Data('spliceDTrainKIS.dat')

    k = 10
    print('------------------------------------')
    print('---------spliceATrainKIS------------')
    print('------------------------------------')
    Test.performTest(d1, k)
    print('------------------------------------')
    print('---------spliceDTrainKIS------------')
    print('------------------------------------')
    Test.performTest(d2, k)
