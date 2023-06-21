"""
Провести дисперсионный анализ для определения того, есть ли различия среднего
роста среди взрослых футболистов, хоккеистов и штангистов. Даны значения роста
в трех группах случайно выбранных спортсменов:
Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.
"""
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

football_players = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey_players = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifters = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166,
                          170])
"""
H0: mu1 = mu2 = mu3
H1: mu1 != mu2
    mu1 != mu3
    mu2 != mu3
Проведем проверку на нормальность
"""
print(stats.shapiro(football_players))
print(stats.shapiro(hockey_players))
print(stats.shapiro(weightlifters))
"""
Pvalue > alfa, H0 не отвергается, распределение во всех выборках нормальное
Проведем проверку на равенство дисперсий
"""
print(stats.bartlett(football_players, hockey_players, weightlifters))
"""
Pvalue > alfa, H0 не отвергается, дисперсии равны
"""
print(stats.f_oneway(football_players, hockey_players, weightlifters))
"""
Pvalue < alfa, при alfa = 0,05, H0 отвергается, средний рост футболистов, 
хоккеистов и штангистоа различен. 
При alfa = 0,01 нулевую гипотеза не отвергается
"""
df = pd.DataFrame({"score": [173, 175, 180, 178, 177, 185, 183, 182, 177, 179,
                             180, 188, 177, 172, 171, 184, 180, 172, 173, 169,
                             177, 166, 180, 178, 177, 172, 166, 170],
                   "group": ["f_p", "f_p", "f_p", "f_p", "f_p", "f_p", "f_p",
                             "f_p", "f_h", "f_h", "f_h", "f_h", "f_h", "f_h",
                             "f_h", "f_h", "f_h", "w", "w", "w", "w", "w", "w",
                             "w", "w", "w", "w", "w"]})
print(df)
tukey = pairwise_tukeyhsd(df["score"], df["group"], alpha=0.05)
print(tukey)
"""
Между футболистами и хоккеистами различий нет, между хоккеистами и штангистами 
различия есть, между футболистами и штангистами различия есть
"""
