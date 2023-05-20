"""
В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом
извлекает 3 детали. Какова вероятность того, что все извлеченные детали
окрашены?
"""
from math import factorial

"""
Формула вероятности P(A)= m/n, где m - число благоприятных исходов, n - общее 
число исходов.
Формула сочетания Ckn=n!/k!(n−k)!
m - это колличество сочетаний 3 деталей из 9
n - это колличество сочетаний 3 деталей из 15
"""

def combination(k, n):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

m = combination(3, 9)
print(f'm = {m}')
n = combination(3, 15)
print(f'n = {n}')
P = m / n
print(f'P = {round(P, 4)} = {round(P * 100, 1)}% ')
