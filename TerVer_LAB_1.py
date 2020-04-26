import numpy as np
from math import *
from PIL import Image


def kombin(t='0'):
    if t == '3':
        print("Перестановки с повторениями")
        n = int(input("Ввод n = "))
        m = []
        i = 0
        while True:
            if sum(m) < n:
                m.append(int(input(' m[' + str(i) + '] = ')))
                i += 1
            else:
                break
        if sum(m) == n:
            C = 1
            for i in range(len(m)):
                m[i] = factorial(m[i])
                C *= m[i]
            P = factorial(n) / C
            image = Image.open("images/033.jpg")
            image.show()
            return P
        else:
            return "Ошибка в начальном условии"
    elif t == '2':
        print("Сочетания без повторений")
        n = int(input("Ввод n = "))
        m = int(input('Ввод m (не больше ' + str(n) + ') = '))
        if 0 <= m <= n:
            C = factorial(n) / (factorial(n - m) * factorial(m))
            image = Image.open("images/4513087.jpeg")
            image.show()
            return C
        else:
            return "Ошибка в начальном условии"
    elif t == '1':
        print("Размещения с повторениями")
        n = int(input("Ввод n = "))
        m = int(input('Ввод m = '))
        A = n ** m
        image = Image.open("images/img-VEdgzz.png")
        image.show()
        return A
    elif t == "4":
        print(" Имеется m операторов и n перенумерованных приборов, которые они могут обслуживать.\n Каждый оператор "
              "выбирает случайным образом и с одинаковой вероятностью любой прибор, но с условием, что ни один "
              "прибор не может обслужи-ваться больше, чем одним оператором.\n Найти вероятность того, что будут "
              "выбраны "
              "для обслуживания приборы с номерами 1, 2, …, m.")
        n = int(input("Кол-во приборов: "))
        m = int(input('Кол-во рабочих (не больше ' + str(n) + ') = '))
        if 0 <= m <= n:
            A = factorial(n) / factorial((n - m))
            image = Image.open('images/fourTask.gif')
            image.show()
            return factorial(m) / A
        else:
            return "Ошибка в начальном условии"
    elif t == "5":
        print("В ящике имеется kТЭЗ, из них k1 элементов 1-го типа, …, ki элементов i-готипа, …, km элементов m-го типа"
              "Из ящика выбирают наугад n ТЭЗ.\nНайти вероятность того, что среди них будет n1 ТЭЗ 1-го типа, …, "
              "ni ТЭЗ i-го типа,…, nm ТЭЗ m-го типа.")
        kel = int(input("Кол - во элементов = "))
        k = []
        i = 0
        while True:
            if sum(k) < kel:
                k.append(int(input(' k[' + str(i) + '] = ')))
                i += 1
            else:
                break
        kt = len(k)
        nt = int(input('берут с ящика (не больше ' + str(kel) + ') = '))
        n = np.zeros(nt)
        for i in range(kt):
            n[i] = int(input(' n[' + str(i) + '] = '))
        Cob = factorial(kel) / (factorial(nt) * factorial(kel - nt))
        C = 1
        for i in range(kt):
            C *= (factorial(k[i]) / (factorial(n[i]) * factorial(k[i] - n[i])))
        image = Image.open('images/CodeCogsEqn.gif')
        image.show()
        return C / Cob
    else:
        return "Такой комбинации не существует"


while True:
    print("Выберите метод:\n "
          "1 - Размещение с повторением\n "
          "2 - Сочетания без повторений\n "
          "3 - Перестановки с повторениями\n"
          'Выберите задачу: \n'
          " 4 - Опрераторы и приборы\n"
          " 5 - ТЭЗ")
    g = input('->')
    print('Ответ = ', kombin(g))
