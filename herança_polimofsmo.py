class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        print("teste")

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca
    def fazer_som(self):
        print("AuAu")

class Gato(Animal):
    def __init__(self,nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca
    def fazer_som(self):
        print("Meeeoooowwww!!!")

meu_cao = Cachorro("Julie", 4, "Poodle")
gato = Gato("Spike", 12, "safadinho")

def emitir_som(animal:Animal):
    animal.fazer_som()

emitir_som(meu_cao)
emitir_som(gato)
