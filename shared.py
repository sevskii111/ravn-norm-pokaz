import numpy as np
    
q = 20

def m(xs):
    return xs.mean()

def g(xs):
    return np.sum((xs - xs.mean()) ** 2) / (len(xs) - 1)

def pemp(xs, a, b, m):
    l = (b - a) / m
    p = np.zeros(m)
    for i in np.arange(0, m):
        p[i] = np.sum([(xs >= (a + l * i)) & (xs < (a + l * (i + 1)))])
    return p / np.sum(p)

def Xi(emp, theor):
    return np.sum((theor - emp) ** 2 / theor)