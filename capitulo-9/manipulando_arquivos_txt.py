

meu_arquivo = open('meu_texto.xlsx', 'x')

meu_arquivo.write('Meu arquivo teste')

meu_arquivo.close()

with open('meu_texto.xlsx', 'a') as file:

    file.writelines(['\nLinha 1', '\nLinha 2', '\nTchau!'])








