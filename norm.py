import pandas as pd
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

c = int(input("m:"))
mean = float(input('M:'))
sigma = float(input('σ:'))
std = sigma ** 2

df = pd.DataFrame(columns=['N', 'M', 'm', '|M - m|', 'D', 'g', '|D - g|', 'δ'])

while True:

    N = int(input("N:"))

    xs = x(mean, sigma, N)

    print(xs[:q])

    mc, gc = m(xs), g(xs)

    pempc = pemp(xs, np.min(xs), np.max(xs), c)
    ptheorc = ptheor(mean, sigma, np.min(xs), np.max(xs), c)

    xi = Xi(pempc, ptheorc)

    df.loc[len(df)] = [N, mean, mc, np.abs(mean - mc), std, gc, np.abs(std - gc), xi]

    print(df)