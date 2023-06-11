"""
Заявляется, что партия изготавливается со средним арифметическим 2,5 см.
Проверить данную гипотезу, если известно, что размеры изделий подчинены
нормальному закону распределения. Объем выборки 10, уровень статистической
значимости 5%   2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34
"""
import numpy as np
from scipy import stats

a = np.array ([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])
mean = np.mean(a)
print(f'среднее = {round(mean, 2)}')
m = 2.5
n = 10
alfa = 0.05
STD = np.std(a, ddof=1)
print(f'стандартное отклонение = {round(STD, 2)}')
t = (mean - m) / (STD / (n ** 0.5))
print(f't наблюдаемое = {round(t, 2)}')
tt = stats.t.ppf(1 - alfa, n - 1)
print(f't критическое = {round(tt, 2)}')
if t < tt:
    print(f't наблюдаемое < t критического, нулевая гипотеза не отвергается,'
          f'статистически значимых отличий нет, '
          f'партия изготавливается со средним = 2,5 см')
else:
    print(f't наблюдаемое > t критического, нулевая гипотеза отвергается,'
          f'статистически значимыe отличия есть, '
          f'партия изготавливается со средним не равным 2,5 см')