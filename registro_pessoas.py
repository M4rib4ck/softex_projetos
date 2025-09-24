class Pessoas:
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade
    def apresentar(self):
        print(f"Seu nome: {self.nome} e idade: {self.idade}")


class Estudantes(Pessoas):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
    def apresentar(self): 
        print(f"Seu nome: {self.nome} e idade: {self.idade} e curso: {self.curso}")

p1= Pessoas("Maria", 19)
curso=Estudantes("Chris", 22, "Engenharia de Software")

lista = [p1,curso]
for pess in lista:
    pess.apresentar()
        