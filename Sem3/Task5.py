"""
Устройство состоит из трех деталей. Для первой детали вероятность выйти из
строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25. Какова
вероятность того, что в первый месяц выйдут из строя:
а). все детали
б). только две детали
в). хотя бы одна деталь
г). от одной до двух деталей?
"""
P1 = 0.1
P2 = 0.2
P3 = 0.25
P = P1 * P2 * P3
print(f'a: все детали = {round(P, 3)}')
P = P1 * P2 * (1 - P3) + P2 * P3 * (1 - P1) + P1 * P3 * (1 - P2)
print(f'б: только 2 детали = {round(P, 3)}')
P = (1 - P1) * (1 - P2) * (1 - P3)
print(f'в: не вышла из строя ни одна деталь = {round(P, 3)}')
P = P1 * (1 - P2) * (1 - P3) + P2 * (1 - P1) * (1 - P3) + P3 * (1 - P1) * \
    (1 - P2)
print(f'вышла из стороя 1 деталь = {round(P, 3)}\nобщая вероятность = '
      f'{0.54 + 0.375}')
print(f'г: от одной до двух деталей = {0.08 + 0.375}')

