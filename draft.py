import numpy as np
from math import *

while True:
    kn = int(input("Кол - во типов = "))
    k = np.zeros(kn)
    for i in range(kn):
            k[i] = int(input(' k[' + str(i) + '] = '))
    kel = int(np.sum(k))
    n = int(input('берут с ящика (не больше ' + str(kel) + ') = '))
    nFind = int(input('Сколько элементов (не больше ' + str(n) + ') = '))
    kFind = int(input('Какой тип (не больше ' + str(kn) + ') = '))
    if nFind <= kFind:
        C = factorial(k[kFind]) / (factorial(nFind) * factorial(k[kFind] - nFind))
        Cob = factorial(kel) / (factorial(n) * factorial(kel - n))
        print(C,'\n', Cob,'\n', C/Cob)
    else:
        print(0)