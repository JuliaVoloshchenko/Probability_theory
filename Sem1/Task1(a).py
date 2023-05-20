"""
Из колоды в 52 карты извлекаются случайным образом 4 карты.
a) Найти вероятность того, что все карты – крести.
"""
from math import factorial

"""
Формула вероятности P(A)= m/n, где m - число благоприятных исходов, n - общее 
число исходов.
Формула сочетания Ckn=n!/k!(n−k)!
52/4 = 13 карт одной масти
m - это колличество способов взять 4 карты из 13
n - это колличество способов взять 4 карты из 52
"""

def combination(k, n):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

m = combination(4, 13)
print(f'm = {m}')
n = combination(4, 52)
print(f'n = {n}')
P = m / n
print(f'P(4 крести) = {round(P, 4)} = {round(P * 100, 2)}%')
