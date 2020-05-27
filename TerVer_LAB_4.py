import numpy as np
from math import *
from PIL import Image
import matplotlib.pyplot as plt

image1 = Image.open('images/srd_kdr.png')
image2 = Image.open('images/dispisya.png')
image3 = Image.open('images/Matozha.png')


def C_bezrepeat(n, m):
    return factorial(n) / (factorial(n - m) * factorial(m))


def binom(n, p):
    q = 1 - p
    M = n * p
    D = n * p * q
    P = []
    for i in range(n + 1):
        P.append(C_bezrepeat(n, i) * p ** i * q ** n - i)
    return M, D, P


def chisl_harac(x, p):
    M = np.sum(x * p)
    M_2 = np.sum((x ** 2) * p)
    D = M_2 - M ** 2
    return M, D


def gip_geo(n, m, k, X):
    p = (C_bezrepeat(m, k) * C_bezrepeat(n - m, X - k)) / C_bezrepeat(n, X)
    return p


def psevd_geo(k, p):
    p = np.array(p)
    q = 1 - p
    k = np.arange(1, k+1)
    P = q ** (k - 1) * p
    P[-1]=1-np.sum(P[:-1])
    return P


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
        m1 = [i for i in range(5)]
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
        for i in range(mk + 1):
            m.append(int(input('m[' + str(i + 1) + '] = ')))
        return pussy(lmbd, m), m


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
        # x.append(int(input('x[' + str(i + 1) + ']= ')))
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
              '\n 1) Вид распределения'
              '\n 2) Решение задач'
              '\n ==> ')
    if w == '1':
        w = input('\n a) Биноминальное'
                  '\n b) Гипергеометрическое'
                  '\n c) Пуассона'
                  '\n d) Псевдогеометрическое'
                  '\n ==> ')
        if w == 'a':
            n = int(input('n = '))
            p = float(input('p = '))
            M, D, p = binom(n, p)
            F = F(range(n+1), p)
            GERAF(range(n+1), F, p)
            print('Математическое ожидание:', np.round(M, 4),
                  '\nДисперсия:', np.round(D, 4),
                  '\nСреднее квадратическое отклонение: ', np.round(sqrt(D), 4),
                  '\nМода:', np.max(p))
        elif w == 'b':
            n = int(input('n = '))
            m = int(input('m = '))
            X = int(input('X = '))
            c = int(input('c = '))
            k = range(c + 1)
            k = np.array(k)
            for i in range(len(k)):
                p = gip_geo(n, m, k[i], X)
                M, D = chisl_harac(k, p)
                print('\nОтвет[' + str(i + 1) + ']:\n', k[i], '\n', np.round(p, 4),)
        elif w == 'c':
            lmbd = float(input())
            c = int(input('Кол-во m: '))
            m = [i for i in range(c + 1)]
            p = pussy(lmbd, m)
            for i in range(len(m)):
                print('\nОтвет[' + str(i + 1) + ']:\n', m[i], '\n', np.round(p[i], 4))
        elif w == 'd':
            k = int(input('k = '))
            p = float(input('p = '))
            M, D = chisl_harac(k, p)
            p = psevd_geo(k, p)
            print(p)
        # image1.show()
        # image2.show()
        # image3.show()
    elif w == '2':
        p, m = pussy_quest()
        for i in range(len(m)):
            print('\nОтвет[' + str(i + 1) + ']:\n', m[i], '\n', np.round(p[i], 4))
