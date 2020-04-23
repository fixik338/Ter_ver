import numpy as np
import sympy as sp


def I_Shooter(p, q):
    s = int(input("Номер стрелка = "))
    q[s - 1] = p[s - 1]
    c = 1
    for i in range(0, 5):
        c *= q[i]
    return c


def OnlyTwoShooters(p, q):
    z = sp.symbols('z')
    f5 = 1
    for i in range(5):
        f5 *= (p[i] * z + q[i])
    f0 = str(sp.expand(f5))
    f = f0.split('*z**2 + ')
    f2 = f[0].split('*z**3 + ')
    return f2[1]


def OnlyOneShooter(p, q):
    c = []
    qs = q
    for i in range(5):
        qs[i] = p[i]
        c.append(np.prod(qs))
        qs[i] = q[i]
    return sum(c)


def Noless4Shooters(p, q):
    z = sp.symbols('z')
    f5 = 1
    for i in range(5):
        f5 *= (p[i] * z + q[i])
    f0 = str(sp.expand(f5))
    f = f0.split('*z**5 + ')
    f2 = f[1].split('*z**4 + ')
    return float(f[0]) + float(f2[0])


def AtLeast1Shooter(p):
    return sum(p)


def terver(t='0'):
    if t == '1':
        print('Найти вероятность безотказной работы схемы, приведенной на рисунке, считая, '
              '\nчто отказы отдельных элементов независимы и вероятность отказа элемента с номером i равна qi.')
        q = []
        p = []
        for i in range(0, 6):
            q.append(float(input('q[' + str(i) + '] = ')))
            p.append(1 - q[i])
        P = p[0] * (p[1] + (p[3] * p[4] * p[5])) * p[2]
        return P
    elif t == '2':
        print('Пять стрелков производят по одному выстрелу в цель. '
              '\nВероятности попада-ния в цель i-ым стрелком соответственно равны pi. '
              '\nНайти вероятность попадания в цель:'
              "\na - только i-го стрелка "
              "\nb - только одного стрелка "
              "\nc - только двух стрелков"
              "\nd - не менее четырех стрелков"
              "\ne - хотя бы одного стрелка.")
        while True:
            g = input("\nВыберите один из пунктов приведенных выше : ")
            p = []
            q = []
            for i in range(0, 5):
                p.append(float(input('p[' + str(i) + '] = ')))
                q.append(1 - p[i])
            if g == 'a':
                print(I_Shooter(p, q))
            elif g == 'b':
                print(OnlyOneShooter(p, q))
            elif g == 'c':
                print(OnlyTwoShooters(p, q))
            elif g == 'd':
                print(Noless4Shooters(p, q))
            elif g == 'e':
                print(AtLeast1Shooter(p))


"------------------------------------------"
while True:
    g = input('Выберите пункт 1 или 2: ')
    print(terver(g))
