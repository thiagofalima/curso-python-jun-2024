
nome = input('Entre com seu nome: ').title()
sobrenome = input('Entre com seu último nome: ').upper()
idade = int(input('Entre com sua idade: '))

print(type(nome))
print(type(sobrenome))
print(type(idade))

msg = f'Oi meu nome é {nome} {sobrenome} e tenho {idade} anos de idade.'

print(msg)
