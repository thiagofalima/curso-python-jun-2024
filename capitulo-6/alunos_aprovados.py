alunos_notas = {'Joao': [7, 4, 5], 'Maria': [5, 8, 9],
                'Leo': [6, 7, 7], 'Pedro': [7, 4, 10]}

# print(*alunos_notas.items(), sep='\n')

alunos_aprovados = dict(filter(
    lambda alunos: round(sum(alunos[1]) / len(alunos[1]), 2) >= 7,
    alunos_notas.items()))

print(alunos_aprovados)
