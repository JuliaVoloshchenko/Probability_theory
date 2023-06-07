"""
Проведите тест гипотезы. Утверждается, что шарики для подшипников,
изготовленные автоматическим станком, имеют средний диаметр 17 мм.
Используя односторонний критерий с α=0,05, проверить эту гипотезу, если
в выборке из n=100 шариков средний диаметр оказался равным 17.5 мм,
а дисперсия генеральной совокупности известна и равна 4 кв. мм.
"""
from scipy import stats

"""
D = 4
sigma = 2
H0: m = m0 = 17
H1: m > 17
Известна ско ген.совокупности, используем z-критерий
"""
z = (17.5 - 17) / (2 / 10)
print(f'z наблюдаемое = {z}')
alfa = 0.05
zt = stats.norm.ppf(1 - alfa)
print(f'z критическое = {round(zt,2)}')
print(f'z наблюдаемое > z критического - нулевая гипотеза отвергается')