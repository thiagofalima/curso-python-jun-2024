

# print('oi')
# input('msg')
# range(1, 10, 1)


def celsius_fahrenheit(c: float, d: float | None = 32) -> float:
    return (1.8 * c) + d


res = celsius_fahrenheit(30)
print(res)


def area_circunferencia(raio=2):

    pi = 3.14

    return pi * raio ** 2


resultado_1 = area_circunferencia()
resultado_2 = area_circunferencia(5)
resultado_3 = area_circunferencia(10)
print(resultado_1)
print(resultado_2)
print(resultado_3)
