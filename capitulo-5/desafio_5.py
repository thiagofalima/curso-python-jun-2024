
lista = []

while True:
    item = input('Entre com um dado (ou enter para sair): ')
    if item:
        lista.append(item)
        continue
    else:
        break

print(lista)

lista_nova = list(set(lista))
print(lista_nova)


lista_nova.sort()

print(lista_nova)
