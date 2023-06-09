"""
Известно, что рост футболистов в сборной распределен нормально с дисперсией
генеральной совокупности, равной 25 кв.см. Объем выборки равен 27, среднее
выборочное составляет 174.2. Найдите доверительный интервал для математического
ожидания с надежностью 0.95.
"""
from scipy import stats

sigma = 5
n = 27
x = 174.2
alfa = 0.05
z = stats.norm.ppf(1 - alfa / 2)
print(f'z = {round(z, 2)}')
a = x - z * (sigma / n ** 0.5)
b = x + z * (sigma / n ** 0.5)
print(f'P({round(a, 2)} < m < {round(b, 2)}) = 0.95')