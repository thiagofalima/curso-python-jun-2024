
def bissexto(ano):

    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        print("É bissexto!")
    else:
        print("Não é bissexto!")


bissexto(2000)
bissexto(2001)


def bissexto():
    ano = int(input("Digite o ano: \n"))
    if ano % 400 == 0:
        print('É bissexto!')
    elif ano % 4 == 0:
        if ano % 100 != 0:
            print('É bissexto!')
        else:
            print('Não é bissexto')
    else:
        print('Não é bissexto!')


bissexto()
