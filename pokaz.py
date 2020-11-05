import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
from shared import *

def ptheor(lam, a, b, m):
    l = (b - a) / m
    p = np.zeros(m)
    for i in np.arange(m):
        left = a + l * i
        right = a + l * (i + 1)
        p[i] = scipy.stats.expon.cdf(right, 0, 1 / lam) - scipy.stats.expon.cdf(left, 0, 1 / lam)
    return p

def x(lam, n):
    return np.random.exponential(1 / lam, n)

def M(lam):
    return lam ** -1

def D(lam):
    return lam ** -2

c = int(input("m:"))
lam = float(input('λ:'))

df = pd.DataFrame(columns=['N', 'M', 'm', '|M - m|', 'D', 'g', '|D - g|', 'δ‎‎‎'])

while True:

    N = int(input("N:"))

    xs = x(lam, N)

    print(xs[:q])

    mean, std = M(lam), D(lam)
    mc, gc = m(xs), g(xs)

    pempc = pemp(xs, np.min(xs), np.max(xs), c)
    ptheorc = ptheor(lam, np.min(xs), np.max(xs), c)

    xi = Xi(pempc, ptheorc)

    df.loc[len(df)] = [N, mean, mc, np.abs(mean - mc), std, gc, np.abs(std - gc), xi]

    print(df)
