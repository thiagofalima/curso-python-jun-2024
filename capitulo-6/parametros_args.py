# def soma(a, b, c, d, e, f) -> int:
#     """
#         Essa função serve para somar 2 argumentos
#     :param a: número real inteiro.
#     :param b: número real inteiro.
#     :param c:
#     :param d:
#     :param e:
#     :return: a soma de a e b.
#     """
#     return a + b + c + d + e + f


def soma(*args: int | None) -> int:
    """

    :param args: números inteiros que formarão um tupla
    :return: a soma de todos os números dessa tupla.
    """
    return sum(args)


res = soma(1, 2, 3, 4, 5, 6, 7, 8)
print(res)
