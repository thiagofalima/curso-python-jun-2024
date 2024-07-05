alunos = {'Joao': [7, 4, 5], 'Maria': [5, 8, 9],
          'Leo': [6, 7, 7], 'Pedro': [7, 4, 10]}


print(alunos.values())

alunos_medias = list(map(lambda notas: round(sum(notas) / len(notas), 2),
                         alunos.values()))

print(alunos_medias)

