
class Animal:

    def __init__(self, classe: str, habitat: str):
        self.classe = classe
        self.habitat = habitat


class Gorila(Animal):

    def __init__(self, classe, habitat, nome, peso):
        super().__init__(classe, habitat)
        self.nome = nome
        self.peso = peso

    def comer(self, alimento):
        print(f'Oi meu nome é {self.nome} e gosto de comer {alimento}')


class Girafa(Animal):

    def __init__(self, classe, habitat, nome, peso):
        super().__init__(classe, habitat)
        self.nome = nome
        self.peso = peso

    def comer(self, alimento: str):
        print(f'Oi meu nome é {self.nome} e gosto de comer {alimento}')


meu_gorila = Gorila('Mamífero', 'Floresta', 'King-kong',
                    500)

print(meu_gorila.habitat)
meu_gorila.comer('Hambuguer')

girafa = Girafa('Mamífero', 'Savana', peso=1500, nome='Melman')

print(girafa.classe)
girafa.comer('Folhas')


