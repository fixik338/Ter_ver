import numpy as np
from math import *
import sympy as sp

p = []
q = []
for i in range(5):
    p.append(float(input('p[' + str(i) + '] = ')))
    q.append(1 - p[i])

z = sp.symbols('z')
f5 = 1
for i in range(5):
    f5 *= (p[i]*z+q[i])
f0 = str(sp.expand(f5))
f = f0.split('*z**2 + ')
f2 = f[0].split('*z**3 + ')
print(f0, '\n', f2[1], f )
