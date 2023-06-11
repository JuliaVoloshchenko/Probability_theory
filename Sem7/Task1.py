"""
Даны две независимые выборки. Не соблюдается условие нормальности
x1 380,420, 290
y1 140,360,200,900
Сделайте вывод по результатам, полученным с помощью функции, имеются ли
статистические различия между группами?
"""
from scipy import stats

x1 = [380, 420, 290]
y1 = [140, 360, 200, 900]
print(stats.mannwhitneyu(x1, y1))
print(f'p-value > alfa, значит нулевая гипотеза не отвергается, '
      f'статистически значимых различий нет')