"""
Проведите тест гипотезы. Продавец утверждает, что средний вес пачки печенья
составляет 200 г.
Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
Известно, что их веса распределены нормально.
Верно ли утверждение продавца, если учитывать, что уровень значимости 1%?
(Провести двусторонний тест.)
"""

import numpy as np
from scipy import stats

"""
H0: m = m0 
H1: m не равно m0
"""
array = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])
average = np.mean(array)
STD = np.std(array, ddof=1)
t = (average - 200) / (STD / len(array) ** 0.5)
print(f't наблюдаемое = {round(t,3)}')
tt1 = stats.t.ppf(0.01 / 2, len(array) - 1)
tt2 = stats.t.ppf(1 - (0.01 / 2), len(array) - 1)
print(f't критическое = {round(tt1, 3)}; {round(tt2, 3)}\n'
      f't наблюдаемое не попало в критичскую область, значит нулевая гипотеза '
      f'не отвергается')

