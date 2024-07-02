a = 42


def minha_funcao():
    global a
    a = 35


minha_funcao()
print(a)

