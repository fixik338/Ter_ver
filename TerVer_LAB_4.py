import numpy as np
from math import *
from PIL import Image
import matplotlib.pyplot as plt

image1 = Image.open('images/srd_kdr.png')
image2 = Image.open('images/dispisya.png')
image3 = Image.open('images/Matozha.png')


def pussy(lmbd, m):
    P = []
    for i in range(len(m)):
        P.append((lmbd ** m[i]) / factorial(m[i]) * np.exp(-lmbd))
    return P


def pussy_quest():
    t = input('a) Задачи'
              '\nb) Ручной ввод'
              '\n ==> ')
    if t == 'a':
        print('Случайная величина Храспределена по закону Пуассона, причем lmbd = 0,2. '
              '\nПостройте часть ряда распределения случайной величины Х для m = 0, 1, 2, 3, 4.')
        lmbd1 = 0.2
        m1 = m = [i for i in range(5)]
        print('\nСлучайная величина Х распределена по закону Пуассона, причем lmbd = 0,8. '
              '\nПостройте часть ряда распределения случайной величины Х для m = 0, 1, 2, 3, 4, 5, 6.')
        lmbd2 = 0.8
        m2 = [i for i in range(7)]
        print('\nСлучайная величина Х распределена по закону Пуассона, причем lmbd = 3. '
              '\nПостройте часть ряда распределения случайной величины Х для m = 0, 1, 2, 3, 4, 5, 6.')
        lmbd3 = 3
        m3 = [i for i in range(7)]
        return [[pussy(lmbd1, m1), pussy(lmbd2, m2), pussy(lmbd3, m3)], [m1, m2, m3]]
    elif t == 'b':
        lmbd = float(input('Значелие лямбды: '))
        mk = int(input('Количество m: '))
        m = []
        for i in range(mk+1):
            m.append(int(input('m[' + str(i+1) + '] = ')))
        return pussy(lmbd, m), m

def Matozha(x, p):
    return np.sum(x * p)


def Matozha_double(x, p):
    return (np.sum((x ** 2) * p))


def Dispisya(a, b):
    return a - b ** 2


def F(x, p):
    a = [0]
    for i in range(2, len(x)):
        a.append(np.sum(p[:i]))
    a.append(np.sum(p))
    return a


def condition():
    X = int(input('Количество возможных значений СВ: '))
    x = [0]
    p = [0]
    for i in range(X):
        x.append(int(input('x[' + str(i + 1) + ']= ')))
        p.append(float(input('p[' + str(i + 1) + ']= ')))
    x = np.array(x)
    p = np.array(p)
    return x, p


def GERAF(x, y, p):
    plt.subplot(2, 1, 1)
    plt.hlines(y[-1], x[-1], 10)
    for i in range(1, len(x)):
        plt.hlines(y[i - 1], x[i - 1], x[i])
    for i in range(1, len(x)):
        plt.vlines(x[i], y[i], y[i - 1], linestyles='--')
    plt.grid(True)
    plt.title('Функция распределения')
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.subplot(2, 1, 2)
    plt.plot(x[1:], p[1:], color='black')
    plt.grid(True)
    plt.title('Многоугольник распределения')
    plt.xlabel('x')
    plt.ylabel('p')
    plt.show()

while True:
    w = input('Выберите: '
              '\n a) График'
              '\n b) Решение задач'
              '\n ==> ')
    if w == 'a':
        x, p = condition()
        M = Matozha(x, p)
        M_2 = Matozha_double(x, p)
        D = Dispisya(M_2, M)
        F = F(x, p)
        GERAF(x, F, p)
        x = x[1:]
        p = p[1:]
        print('Математическое ожидание:', np.round(M, 4),
              '\nДисперсия:', np.round(D, 4),
              '\nСреднее квадратическое отклонение: ', np.round(sqrt(D), 4),
              '\nМода:', np.max(p))
        image1.show()
        image2.show()
        image3.show()
    elif w == 'b':
        p, m = pussy_quest()
        for i in range(len(m)):
            print('\nОтвет['+str(i+1)+']:\n',  m[i], '\n', np.round(p[i], 4))