senha = input('Cadastre uma senha de 6: \n')

while len(senha) != 6:
    senha = input('Quantidade de char inválida \n'
                  'Cadastre uma senha de 6: \n')

print('Cadastro realizado com sucesso!')

