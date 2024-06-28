
# num = int(input('Informe o tamanho de sua lista: '))
# minha_lista = []
#
# for numero in range(1, num + 1):
#     minha_lista.append(numero)
#
# print(minha_lista)
#
# for elemento in minha_lista:
#     if elemento % 2 == 0:
#         minha_lista.remove(elemento)
#
# print(minha_lista)

# import time
#
# lista = []
#
# for i in range(1, 6):
#     lista.append(i)
#     print(lista)
#     time.sleep(1)
#
# for i in range(5, 1, -1):
#     lista.remove(i)
#     print(lista)
#     time.sleep(1)

# Enumerate

lista = list(range(21))

print(lista)

for indice, valor in enumerate(lista):
    print(indice, valor)
