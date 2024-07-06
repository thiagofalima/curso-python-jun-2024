import matplotlib.pyplot as plt

linguagens = ['c++', 'c#', 'python', 'java', 'go']
votos = sorted([100, 150, 350, 50, 65], reverse=True)
cores = ["#03AED2", "#68D2E8", "#FDDE55", "#FEEFAD", "#03AED2"]

fig, ax = plt.subplots()

print(fig)
print(ax)

grafico = ax.bar(linguagens, votos, color=cores, align='edge', width=0.5)
ax.set_title('linguagens de programação x quantidade de votos')
ax.set_xlabel('linguagens de programação')
ax.set_ylabel('votos por linguagens')
ax.bar_label(grafico, padding=3)
ax.set_ylim(0, 500)
# ax.bar_label(grafico, padding=3)
plt.show()
