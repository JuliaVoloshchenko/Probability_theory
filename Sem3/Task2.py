"""
В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике -
12 мячей, из которых 5 белых. Из первого ящика вытаскивают случайным образом
два мяча, из второго - 4 мяча. Какова вероятность того, что 3 мяча белые?
"""
from math import factorial

def combination(k, n):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

"""
P1 - из первой корзины не вытащили ни одного белого мяча, из второй вытащили 
3 белых мяча;
P2 - из первой корзины вытащили 1 белый мяч, из второй вытащили 2 белых мяча;
P3 - из первой корзины вытащили 2 белых мяча, из второй вытащили 1 белый мяч.
"""
P1 = (combination(2, 3) / combination(2, 8)) * (combination(3, 5) *
     combination(1, 7) / combination(4, 12))
P2 = (combination(1, 5) * combination(1, 3) * combination(2, 5) *
      combination(2, 7)) / (combination(2, 8) * combination(4, 12))
P3 = (combination(2, 5) * combination(1, 5) * combination(3, 7)) / \
     (combination(2, 8) * combination(4, 12))
P = P1 + P2 + P3
print(f'P = {round (P,4)} = {round(P * 100, 2)}%')