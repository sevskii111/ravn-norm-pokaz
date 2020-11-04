import matplotlib.pyplot as plt
import numpy as np
from shared import *

def ptheor(a, b, m):
    return np.full(m, 1 / m)

def x(a, b, r):
    return a + r * ((a * b - 1) / a)

def M(a, b):
    return (a + b) / 2

def D(a, b):
    return (b - a) ** 2 / 12

N = int(input("N:"))
c = int(input('m:'))
a = int(input('a:'))
b = int(input('b:'))

rs = np.random.rand(N)

xs = x(a, b, rs)

Mc, Dc, mc, gc = M(a, b), D(a, b), m(xs), g(xs)

pempc = pemp(xs, a, b, c)
ptheorc = ptheor(a, b, c)

xi = Xi(pempc, ptheorc)

print(Mc, Dc, mc, gc, xi)

plt.plot(pempc)
plt.plot(ptheorc)
plt.show()
