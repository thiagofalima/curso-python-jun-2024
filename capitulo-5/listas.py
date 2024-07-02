
# print(ord('c'))
# print(ord(' '))

# minha_lista = [1, 2, 3, 4, 5]
#
# print(minha_lista)
# print(type(minha_lista))
#
# print(minha_lista[2])
# print(minha_lista[1])
# print(minha_lista[-1])
#
# nome = 'Thiago'
#
# print(nome[-1])

# Slicing

# print(minha_lista[0:4])
#
# minha_lista_2 = list(range(1, 21))
#
# print(minha_lista_2)
#
# print(minha_lista_2[1:12:2])
#
# print(sum(minha_lista_2))
# print(max(minha_lista_2))
# print(min(minha_lista_2))

# Métodos

minha_lista_2 = list(range(1, 11))
print(minha_lista_2)

minha_lista_2.append(11)

print(minha_lista_2)

# minha_lista_2.append([12, 13, 14])

minha_lista_2.extend([12, 13, 14])

print(minha_lista_2)

minha_lista_2.insert(5, 'inserido')
print(minha_lista_2)

print(minha_lista_2.index(8))

minha_lista_2.remove('inserido')

print(minha_lista_2)

ultimo = minha_lista_2.pop()

print(ultimo)
print(minha_lista_2)

del minha_lista_2[2]

print(minha_lista_2)

minha_lista_2 = minha_lista_2 + [1, 2, 3]

print(minha_lista_2)

nomes = ['Telma', 'Gustavo', 'Nathália', 'Peter', 'Alexandre', 'Fernando']

nomes.sort(reverse=True)

print(nomes)



