
# Operadores Booleanos

# Unir condições lógicas ou avaliações.

# AND

print(2 == 2 and 3 > 10)
#
acesso = True
credenciais = False
#
print(acesso and credenciais)
#
if acesso:
    if credenciais:
        print('Bm-vindo')
    else:
        print('Sai fora!')

# OR

print(2 > 3 or 3 == 5 or 10 > 1)

print(12 > 3 or 3 == 5 or 10 > 1 and 3 % 2 == 0)

# NOT

print(not 3 == 3)

print(not (12 > 3 or 3 == 5 or 10 > 1 and 3 % 2 == 0))





