import numpy as np
from math import *
def I_Shooter(p,q):
    s = int(input("Номер стрелка = "))
    q[s] = p[s]
    c = 1
    for i in range(1,6):
        c *= q[i]
    return c
def OnlyTwoShooters(p, q):


def OnlyOneShooter(p, q):
    c = []
    qs = q
    for i in range(1,6):
        qs[i] = p[i]
        c.append(prod(qs))
        qs[i] = q[i]
    return sum(c)


def Noless4Shooters(p, q):



def AtLeast1Shooter(p, q):
    return sum(p)


def terver(t='0'):
    if t == '1':
        q = []
        p = []
        for i in range(1, 7):
            q.append(float(input('q[' + str(i) + '] = ')))
            p.append(1 - q[i])
        P = p[1]*(p[2]+(p[4]*p[5]*p[6]))*p[3]
        return P
    if t == '2':
        p = []
        q = []
        for i in range(1, 6):
            p.append(float(input('p[' + str(i) + '] = ')))
            q.append(1-p[i])
        while True:
            print("Выберите пункт:\n "
                  "a - только i-го стрелка\n "
                  "b - только одного стрелка\n "
                  "c - только двух стрелков\n "
                  "d - не менее четырех стрелков\n "
                  "e - хотя бы одного стрелка.")
            g = input()
            if g == 'a':
                print(I_Shooter(p, q))
            elif g == 'b':
                print(OnlyOneShooter(p, q))
            elif g == 'c':
                print(OnlyTwoShooters(p, q))
            elif g == 'd':
                print(Noless4Shooters(p, q))
            elif g == 'e':
                print(AtLeast1Shooter(p, q))
"------------------------------------------"
while True:
   g = input()
   print(terver(g))