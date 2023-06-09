"""
 Вероятность того, что лампочка перегорит в течение первого дня эксплуатации,
 равна 0.0004. В жилом комплексе после ремонта в один день включили 5000 новых
 лампочек. Какова вероятность, что ни одна из них не перегорит в первый день?
 Какова вероятность, что перегорят ровно две?
"""
from math import factorial

def pyasson(m, n, p):
    lamb = n * p;
    e = 2.72;
    return lamb ** m / factorial(m) * e ** (-lamb)

P1 = pyasson(0, 5000, 0.0004)
P2 = pyasson(2, 5000, 0.0004)
print(f'P1 {round(P1, 3)} = {round(P1 * 100, 1)}%')
print(f'P2 {round(P2, 3)} = {round(P2 * 100, 1)}%')
