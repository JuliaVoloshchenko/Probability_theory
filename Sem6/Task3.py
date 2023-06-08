"""
Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175

Используя эти данные построить 95% доверительный интервал для разности среднего
роста родителей и детей.
"""
import numpy as np
from scipy import stats

daughters = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
mothers = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
n1 = n2 = n = 10
alfa = 0.05
x1 = np.mean(daughters)
x2 = np.mean(mothers)
print(f'среднее дочери {x1}, среднее матери {x2}')
delta = x2 - x1
print(f'дельта = {round(delta, 2)}')
D1 = (np.std(daughters, ddof=1)) ** 2
D2 = (np.std(mothers, ddof=1)) ** 2
print(f'D1 = {round(D1, 2)}, D2 = {round(D2, 2)}')
D = (D1 + D2) / 2
print(f'D общее = {round(D, 2)}')
S = ((D / n) + (D / n)) ** 0.5
print(f'S = {round(S, 2)}')
t = stats.t.ppf(1 - alfa / 2, 2 * (n - 1))
print(f't = {round(t, 2)}')
a = delta - t * S
b = delta + t * S
print(f'P({round(a, 2)} < m < {round(b, 2)}) = 0.95')