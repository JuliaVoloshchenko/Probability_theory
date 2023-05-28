"""
Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в
цель ровно 85 раз.
"""
from math import factorial

"""
Формула Бернули Pn(X=k) = Ckn p**k q**n-k
"""

def bernuli(n, k, p):
    combination = factorial(n) / (factorial(k) * factorial(n - k));
    return combination * (p ** k) * (1 - p) ** (n - k)

P = bernuli(100, 85, 0.8)
print(f'P = {round(P, 3)} = {round(P * 100, 1)}%')
