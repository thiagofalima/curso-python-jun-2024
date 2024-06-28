idade = int(input("Entre com sua idade: "))
cnh = False

if idade >= 65:
    if cnh:
        print('Renove a carta a cada 5 anos.')
    else:
        pass
elif 65 > idade >= 18:
    if cnh:
        print('Renove a carta a cada 10 anos.')
    else:
        pass
else:
    print('Tire a carta se quiser quando for maior de 18.')

