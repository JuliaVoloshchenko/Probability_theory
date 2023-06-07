"""
Есть ли статистически значимые различия в среднем росте матерей и
дочерей?
Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169, 165
Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160, 163
"""
from scipy import stats

mothers = [172, 177, 158, 170, 178,175, 164, 160, 169, 165]
daughters = [173, 175, 162, 174, 175, 168, 155, 170, 160, 163]
print(stats.ttest_ind(mothers, daughters))
print(f'pvalue > alfa, значит нулевая гипотеза не отвергается, '
      f'статистически значимых различий нет')