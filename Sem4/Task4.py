"""
 Рост взрослого населения города X имеет нормальное распределение, причем,
 средний рост равен 174 см, а среднее квадратическое отклонение равно 8 см.
 посчитайте, какова вероятность того, что случайным образом выбранный взрослый
 человек имеет рост:
1. больше 182 см?
2. больше 190 см?
3. от 166 см до 190 см?
4. от 166 см до 182 см?
5. от 158 см до 190 см?
6. не выше 150 см или не ниже 190 см?
7. не выше 150 см или не ниже 198 см?
8. ниже 166 см?

Задачу можно решить двумя способами: без использования сторонних библиотек
(numpy, scipy, pandas и пр.), а затем проверить себя с помощью встроенных
функций
"""
from scipy import stats

print(f'1. P = {1 - stats.norm.cdf(182, loc=174, scale=8)}')

print(f'2. P = {1 - stats.norm.cdf(190, loc=174, scale=8)}')

Pa = stats.norm.cdf(166, loc=174, scale=8)
Pb = stats.norm.cdf(190, loc=174, scale=8)
print(f'3. P = {Pb - Pa}')

Pc = stats.norm.cdf(182, loc=174, scale=8)
print(f'4. P = {Pc - Pa}')

Pd = stats.norm.cdf(158, loc=174, scale=8)
print(f'5. P = {Pb - Pd}')

Pe = stats.norm.cdf(150, loc=174, scale=8)
Pf = 1 - stats.norm.cdf(190, loc=174, scale=8)
print(f'6. P = {Pe + Pf}')

Pj = 1 - stats.norm.cdf(198, loc=174, scale=8)
print(f'7. P = {Pe + Pj}')

print(f'8. P = {stats.norm.cdf(166, loc=174, scale=8)}')
