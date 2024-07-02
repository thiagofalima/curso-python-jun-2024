
# meu_dicionario = {'k1': 'valor1', 'k2': 'valor2', 'k3': 'valor3'}
#
# print(meu_dicionario)
# print(type(meu_dicionario))
#
# print(len(meu_dicionario))
#
# print(meu_dicionario['k2'])
#
# res = meu_dicionario['k2']
#
# print(res)
#
# meu_dicionario['k2'] = 'novo valor'
#
# print(meu_dicionario)
#
# del meu_dicionario['k2']
#
# print(meu_dicionario)

d = {1: 'Thiago',
     2: 'Gabriel',
     3: 'Gustavo',
     4: 'Telma',
     5: 'Nathália',
     6: 'Peter',
     7: 'FF',
     8: 'FM',
     9: 'Alexandre'}

print(d.items())

for chave, valor in d.items():
    print(chave, valor, sep='->')

print(d.keys())
print(d.values())

d[10] = 'Novo aluno'

print(d)

del d[10]

print(d)


