
def notas_alunos(**kwargs: int | float) -> dict:

    for aluno, nota in kwargs.items():

        print(f'{aluno} tirou {nota} na prova p1.')

    return kwargs


meus_alunos = notas_alunos(joao=7, maria=8.5)

print(meus_alunos)
