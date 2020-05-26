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
            if q[i] < 0:
                print("Ошибка: вероятность не может быть отридцательной.")
                quit()
            if np.sum(q) > 1:
                print("Ошибка: общая вероятность не может быть больше 1.")
                quit()
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
                if q[i] < 0:
                    print("Ошибка: вероятность не может быть отридцательной.")
                    quit()
                if np.sum(q) > 1:
                    print("Ошибка: общая вероятность не может быть больше 1.")
                    quit()
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
    elif t == '3':
        print(
            "Определить надёжность схемы, указанной на рисунке, считая, "
            "\nчто все элементы работают независимо друг от друга."
            "\nВероятность отказа i-го элемента равна qi.")
        q = []
        p = []
        print("\nВведите вероятность поломки...")
        for i in range(0, 5):
            q.append(float(input("" + str(i + 1) + "-го элемента: ")))
            if q[i] < 0:
                print("Ошибка: вероятность не может быть отридцательной.")
                quit()
            if np.sum(q) > 1:
                print("Ошибка: общая вероятность не может быть больше 1.")
                quit()
            p.append(1 - q[i])
        P = p[0] * p[3] * (((p[1] + p[2])) * p[4])
        return P
    elif t == '4':
        k = int(input('Выберите задачу:'
                      '\nЗадача 1. \nИмеются три урны с шарами. В первой урне 4 белых и 5 черных, во'
                      '\nвторой – 5 белых и 4 черных, в третьей – 6 белых шаров. Некто выбирает наугад одну из'
                      '\nурн и вынимает из нее шар. Найти вероятность того, что: а) этот шар окажется белым, б)'
                      '\nбелый шар вынут из второй урны.'

                      '\n\nЗадача 2. \nОднотипные приборы выпускаются 3 заводами в отношении 3:4:5,'
                      '\nпричѐм вероятность брака для этих заводов соответственно равны 0,04; 0,05; 0,03.'
                      '\nПриобретѐнный прибор оказался бракованным. Какова вероятность того, что он'
                      '\nизготовлен 3-м заводом.'

                      '\n==>'))
        if k == 1:
            k = (int(input('Кол - во урн: ')))
            p1 = []
            p2 = []
            white = []
            black = []
            for i in range(k):
                white.append(float(input("Количество белых шаров в урне № " + str(i + 1) + '\n==>')))
                black.append(float(input("Количество черных шаров в урне № " + str(i + 1) + '\n==>')))
                p1.append(1 / k)
                p2.append(white[i] / (white[i] + black[i]))
            P = np.sum(np.array(p1) * np.array(p2))
            PB = (p1[1] * p2[1]) / P
            return 'a) = ' + str(P), 'b) = ' + str(PB)
        elif k == 2:
            k = (int(input('Кол - во заводов:  ')))
            p1 = []
            p2 = []
            b = []
            for i in range(k):
                b.append(float(input("Количество изготавливаемых деталей завода № " + str(i + 1) + '\n==>')))
                p2.append(float(input("Вероятность брака детали на заводе № " + str(i + 1) + '\n==>')))
            bs = np.sum(np.array(b))
            for i in range(k):
                p1.append(b[i] / bs)
            P = np.sum(np.array(p1) * np.array(p2))
            PB = (p1[2] * p2[2]) / P
            return 'a) = ' + str(P), 'b) = ' + str(PB)


"------------------------------------------"
while True:
    g = input('\nВыберите пункт: '
              '\n1 - задача про схему'
              '\n2 - задача про стрелков'
              '\n3 - своя задача на надежность цепи'
              '\n4 - формула полной вероятности и байеса'
              '\n==> ')
    if g < str(1) or g > str(4):
        print('Ошибка: введите один из заданных номеров пунктов.')
        quit()
    print('Ответ:', terver(g))
