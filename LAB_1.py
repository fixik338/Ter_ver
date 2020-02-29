import numpy as np
from math import *
from PIL import Image


def kombin(t='0'):
    if t == '3':
        print("Перестановки с повторениями")
        n = int(input("Enter n = "))
        k = int(input('Enter k = '))
        m = np.zeros(k)
        for i in range(k):
            m[i] = int(input(' m[' + str(i) + '] = '))
        if 0 <= len(m) <= n:
            C = 1
            for i in range(len(m)):
                m[i] = factorial(m[i])
                C *= m[i]
            P = factorial(n) / C
            image3 = Image.open("images/033.jpg")
            image3.show()
            return P
        else:
            return "Ошибка в начальном условии"
    elif t == '2':
        print("Сочетания без повторений")
        n = int(input("Enter n = "))
        m = int(input('Enter m = '))
        if 0 <= m <= n:
            C = factorial(n) / (factorial(n - m) * factorial(m))
            image2 = Image.open("4513087.jpeg")
            image2.show()
            return C
        else:
            return "Ошибка в начальном условии"
    elif t == '1':
        print("Размещения с повторениями")
        n = int(input("Enter n = "))
        m = int(input('Enter m = '))
        A = n ** m
        image1 = Image.open("images/img-VEdgzz.png")
        image1.show()
        return A
    elif t == "419":
        print("Имеется m операторов и n перенумерованных приборов, которые они могут обслуживать. Каждый оператор "
              "выбирает случайным образом и с одинаковой ве-роятностью любой прибор, но с условием, что ни один "
              "прибор не может обслужи-ваться больше, чем одним оператором. Найти вероятность того, что будут выбраны "
              "для обслуживания приборы с номерами 1, 2, …, m.")
        n = int(input("Кол-во приборов: "))
        m = int(input("Кол-во рабочих: "))
        if 0 <= m <= n:
            P = factorial(n) / factorial((n - m))
            return factorial(m) / P
        else:
            return "Ошибка в начальном условии"
    elif t == "5":
        print("В ящике имеется kТЭЗ, из них k1 элементов 1-го типа, …, ki элементов i-готипа, …, km элементов m-го типа"
              "Из ящика выбирают наугад n ТЭЗ.Найти вероятность того, что среди них будет n1 ТЭЗ 1-го типа, …, "
              "ni ТЭЗ i-го типа,…, nm ТЭЗ m-го типа.")
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