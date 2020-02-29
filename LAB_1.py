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
            print('m', '[', i + 1, ']', '=', end=' ')
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
        print("Перестановки с повторениями")
        k = int(input('Enter k = '))
        n = int(input('Enter n = '))
        m = np.zeros(k)
        for i in range(k):
            print('m', '[', i + 1, ']', '=', end=' ')
            m[i] = int(input())
            for i in range(n):
                m[i] = factorial(m[i])
                C *= m[i]
            P = factorial(n) / C
            return P
        else:
            return "Ошибка в начальном условии"
    else:
        return "Такой комбинации не существует"


print("Выберите метод:\n 1 - Размещение с повторением\n 2 - Сочетания без повторений\n 3 - Перестановки с повторениями")
while True:
    g = input()
    print(kombin(g))
