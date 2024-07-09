import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplcursors

df = pd.read_excel('notas.xlsx')

# print(len(df))
#
# for i in range(len(df)):
#     print(df.iloc[i]['cidade'])

print(df)
print(df['nota-1'])
print(type(df['nota-1']))

array_notas_1 = np.array(df['nota-1'])
array_notas_2 = np.array(df['nota-2'])


print(array_notas_1)
print(array_notas_2)

array_medias = (array_notas_1 + array_notas_2) / 2

print(array_medias)

print(df)

df['media'] = array_medias

print(df)

df['status'] = ['Aprovado' if media >= 6 else 'Recuperacao'
                for media in df['media']]

print(df)

df.to_excel('notas_medias.xlsx')

cores = ['#402E7A', '#5A639C', '#7776B3', '#9B86BD', '#E2BBE9', '#E8C5E5']

fig, ax = plt.subplots()

grafico = ax.bar(df['nome'], df['media'], color=cores, width=0.5)
ax.set_title('Alunos x Médias')
ax.set_xlabel('Alunos')
ax.set_ylabel('Médias')
ax.set_ylim(0, 10)
ax.bar_label(grafico, padding=0.3)
mplcursors.cursor(hover=True).connect(
    "add", lambda sel: sel.annotation.set_text(df['status'][sel.index]))
plt.show()
