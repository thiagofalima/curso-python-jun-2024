# TODO: Receber 3 lados de um triângulo

a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))

# TODO: Verificar se é triângulo

if (a + b > c) or (b + c > a) or (c + a > b):
    print('É um triângulo')

#   TODO: Verificar o tipo
#   Equilátero
    if a == b == c:
        print('Equilátero')
    # Isóceles
    elif a == b or b == c or c == a:
        print('Isceles')
    # Escaleno
    elif a != b or b != c or c != a:
        print('Escaleno')


