
# lista_pares = []
# for numero in lista:
#     if numeros_pares(numero):
#         lista_pares.append(numero)
#     else:
#         pass

# def numeros_pares(num):
#     return num % 2 == 0


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_pares = list(filter(lambda x: x % 2 == 0, lista))

print(lista_pares)
