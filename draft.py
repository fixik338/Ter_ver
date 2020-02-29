import numpy as np
from math import *

while True:
    kel = int(input('количество элементов = '))
    kn = int(input('типов (не больше ' + str(kel) + ') = '))
    n = int(input('берут с ящика (не больше ' + str(kel) + ') = '))
    k = np.zeros(kn)
    for i in range(kn):
        if np.sum(k) < kel:
            k[i] = int(input(' k[' + str(i) + '] = '))
        else:
            break
    nFind = int(input('Сколько элементов (не больше ' + str(n) + ') = '))
    kFind = int(input('Какой тип (не больше ' + str(kn) + ') = '))
    C = (factorial(k[kFind]) / (factorial(nFind) * factorial(k[kFind] - nFind)))
    Cob = factorial(kel) / (factorial(n) * factorial(kel - n))
    P = factorial(kel)
    print(C,'\n', Cob,'\n', C/Cob)
