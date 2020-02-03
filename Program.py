"""
@file Program.py
@author Marcin Kretkowski, Adrianna Łukaszuk
"""

from Data import Data
from Test import Test

if __name__ == "__main__":
    d1 = Data('spliceATrainKIS.dat')
    d2 = Data('spliceDTrainKIS.dat')

    for k in range(2, 11, 2):
        print('-------------------------------------------')
        print('-------------spliceATrainKIS---------------')
        print('-------------------------------------------')
        print(f'----------{k}-fold cross validation----------')
        print('-------------------------------------------')
        Test.performTest(d1, k)

    for k in range(2, 11, 2):
        print('-------------------------------------------')
        print('-------------spliceDTrainKIS---------------')
        print('-------------------------------------------')
        print(f'----------{k}-fold cross validation----------')
        print('-------------------------------------------')
        Test.performTest(d2, k)
   
 
