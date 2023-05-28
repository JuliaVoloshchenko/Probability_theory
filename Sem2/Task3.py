"""
Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
"""
from math import factorial

"""
Формула Бернули Pn(X=k) = Ckn p**k q**n-k
"""

def bernuli(n, k, p):
    combination = factorial(n) / (factorial(k) * factorial(n - k));
    return combination * (p ** k) * (1 - p) ** (n - k)

P = bernuli(144, 70, 0.5)
print(f'P = {round(P, 3)} = {round(P * 100, 1)}%')
