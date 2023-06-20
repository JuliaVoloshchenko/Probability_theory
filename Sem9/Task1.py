"""
Даны значения величины заработной платы заемщиков банка (zp) и значения их
поведенческого кредитного скоринга (ks):
zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
Используя математические операции, посчитать коэффициенты линейной регрессии,
приняв за X заработную плату (то есть, zp - признак), а за y - значения
скорингового балла (то есть, ks - целевая переменная). Произвести расчет как
с использованием intercept, так и без.
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
"""
Построим график, что бы посмотреть, есть ли линейная зависимость
"""
plt.scatter(zp, ks)
plt.xlabel('Величина заработной платы')
plt.ylabel('Поведенческий кредитный скоринг')
plt.show()

b = (np.mean(zp * ks) - np.mean(zp) * np.mean(ks)) / (np.mean(zp ** 2) -
                                                      np.mean(zp) ** 2)
print(f'коэффициент b = {round(b, 2)}')
a = np.mean(ks) - b * np.mean(zp)
print(f'интерсепт a = {round(a, 2)}')
"""
Отобразим функцию линейной зависимости на графике
"""
plt.scatter(zp, ks)
plt.plot(zp, a + b * zp, c='r')
plt.xlabel('Величина заработной платы')
plt.ylabel('Поведенческий кредитный скоринг')
plt.show()
"""
Решение с помощью модели линейной регрессии
"""
x = zp.reshape(-1, 1)
y = ks.reshape(-1, 1)
model = LinearRegression()
model.fit(x, y)
r_sq = model.score(x, y)
print(f'R2 = {r_sq}')
a = model.intercept_
print(f'const = {a}')
b = model.coef_
print(f'beta = {b}')
plt.scatter(x, y)
plt.suptitle(f'R2 = {r_sq}')
plt.plot(x, a + b * x, c='r')
plt.xlabel('Величина заработной платы')
plt.ylabel('Поведенческий кредитный скоринг')
plt.show()
"""
Без интерсепта
"""
x = zp.reshape(-1, 1)
y = ks.reshape(-1, 1)
model = LinearRegression()
model.fit(x, y)
r_sq = model.score(x, y)
print(f'R2 = {r_sq}')
b = model.coef_
print(f'beta = {b}')
plt.scatter(x, y)
plt.suptitle(f'R2 = {r_sq}')
plt.plot(x, b * x, c='r')
plt.xlabel('Величина заработной платы')
plt.ylabel('Поведенческий кредитный скоринг')
plt.show()
