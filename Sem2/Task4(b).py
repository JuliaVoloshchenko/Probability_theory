"""
 В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике -
 11 мячей, из которых 9 белых. Из каждого ящика вытаскивают случайным образом
 по два мяча.
 b. Какова вероятность того, что ровно два мяча белые?
"""
from math import factorial

"""
Подсчитаем общее число исходов при вытаскивании мячей:
n1 - это колличество сочетаний 2 из 10
n2 - это колличество сочетаний 2 из 11
"""

def combinations(k, n):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

n1 = combinations(2, 10)
n2 = combinations(2, 11)
"""
m1 - это колиичество сочетаний 2 из 7
m2 - это колиичество сочетаний 2 из 9
P = P(A)*P(B)+P(C)*P(D)+P(E)*P(F)
"""
m_A = combinations(2, 7)
m_B = combinations(2, 2)
m_C = combinations(1, 7) * combinations(1, 3)
m_D = combinations(1, 9) * combinations(1, 2)
m_E = combinations(2, 3)
m_F = combinations(2, 9)
P = (m_A / n1) * (m_B / n2) + (m_C / n1) * (m_D / n2) + (m_E / n1) * (m_F / n2)
print(f'Р = {round(P, 4)} = {round(P * 100, 1)}%')
