import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
from shared import *

def ptheor(mean, std, a, b, m):
    l = (b - a) / m
    p = np.zeros(m)
    for i in np.arange(m):
        left = a + l * i
        right = a + l * (i + 1)
        p[i] = scipy.stats.norm.cdf(right, mean, std) - scipy.stats.norm.cdf(left, mean, std)
    return p

def x(mean, std, n):
    return np.random.normal(mean, std, n)

def M(a, b):
    return (a + b) / 2

def D(a, b):
    return (b - a) ** 2 / 12

N = int(input("N:"))
c = int(input("m:"))
mean = int(input('M:'))
std = int(input('σ:'))

xs = x(mean, std, N)

mc, gc = m(xs), g(xs)

pempc = pemp(xs, np.min(xs), np.max(xs), c)
ptheorc = ptheor(mean, std, np.min(xs), np.max(xs), c)

print(pempc, ptheorc)

xi = Xi(pempc, ptheorc)

print(mean, std, mc, gc, xi)

plt.plot(pempc)
plt.plot(ptheorc)
plt.show()