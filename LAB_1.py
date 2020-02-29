"  задачи 2 и 5(2 ч)"
import numpy as np
import sympy as sp
from math import *


def kombin(t=0):
    if t == '3':
        print("Перестановки с повторениями")
        n = int(input("Enter n = "))
        k = int(input('Enter k = '))
        m = np.zeros(k)
        for i in range(k):
            print('m', '[', i, ']', '=', end=' ')
            m[i] = int(input())
        if 0 <= len(m) <= n:
            C = 1
            for i in range(len(m)):
                m[i] = factorial(m[i])
                C *= m[i]
            P = factorial(n) / C
            return P
        else:
            return "Ошибка в начальном условии"
    elif t == '2':
        print("Сочетания без повторений")
        n = int(input("Enter n = "))
        m = int(input('Enter m = '))
        if 0 <= m <= n:
            C = factorial(n) / (factorial(n - m) * factorial(m))
            return C
        else:
            return "Ошибка в начальном условии"
    elif t == '1':
        print("Размещения с повторениями")
        n = int(input("Enter n = "))
        m = int(input('Enter m = '))
        A = n ** m
        return A
    elif t == "419":
        print("Мужички начинают работать...")
        n = int(input("Кол-во приборов: "))
        m = int(input("Кол-во рабочих: "))
        if 0 <= m <= n:
            P = factorial(n) / factorial((n - m))
            return factorial(m) / P
        else:
            return "Ошибка в начальном условии"
    elif t == "5":
        print("Детали ожидают своей материализации и работы над ними")
        kn = int(input("Кол - во типов = "))
        k = np.zeros(kn)
        for i in range(kn):
            k[i] = int(input(' k[' + str(i) + '] = '))
        kel = int(np.sum(k))
        n = int(input('берут с ящика (не больше ' + str(kel) + ') = '))
        kFind = int(input('Какой тип (не больше ' + str(kn) + ') = '))
        nFind = int(input('Сколько элементов (не больше ' + str(int(k[kFind])) + ') = '))
        if nFind <= k[kFind]:
            C = factorial(k[kFind]) / (factorial(nFind) * factorial(k[kFind] - nFind))
            Cob = factorial(kel) / (factorial(n) * factorial(kel - n))
            return C / Cob
        else:
            return 0
    else:
        return "Такой комбинации не существует"



while True:
    print("Выберите метод:\n "
          "1 - Размещение с повторением\n "
          "2 - Сочетания без повторений\n "
          "3 - Перестановки с повторениями\n"
          "419 - Мужички\n"
          "5 - Детали")
    g = input()
    print(kombin(g))
