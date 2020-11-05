import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from shared import *

def ptheor(a, b, m):
    return np.full(m, 1 / m)

def x(a, b, r):
    return np.random.uniform(a, b, r)

def M(a, b):
    return (a + b) / 2

def D(a, b):
    return (b - a) ** 2 / 12

c = int(input('m:'))
a = float(input('a:'))
b = float(input('b:'))

df = pd.DataFrame(columns=['N', 'M', 'm', '|M - m|', 'D', 'g', '|D - g|', 'δ‎‎‎'])

while True:
    N = int(input("N:"))

    xs = x(a, b, N)

    print(xs[:q])

    mean, std, mc, gc = M(a, b), D(a, b), m(xs), g(xs)

    pempc = pemp(xs, a, b, c)
    ptheorc = ptheor(a, b, c)

    xi = Xi(pempc, ptheorc)

    df.loc[len(df)] = [N, mean, mc, np.abs(mean - mc), std, gc, np.abs(std - gc), xi]

    print(df)