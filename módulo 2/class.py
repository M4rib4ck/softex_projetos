class Cachorro:
    def __init__(self, nome_cachorrinho: str, cor_pelo: str, idade_c:int):
        self.nome = nome_cachorrinho #atributo nome recebe o nome do cachorro q veio de um parametro
        self.cor = cor_pelo
        self.idade = idade_c
    def latir(self, fala: str) -> None:
        print(f"{self.nome} diz {fala}!")

meu_cachorro = Cachorro("Julie", "Branca", 13)
rex = Cachorro("Rex", "marrom", 1) # rex é do tipo cachorro, recebe os atributos da classe
selena = Cachorro("Selena", "Preta", 1)

print(f"Nome:{meu_cachorro.nome}, Cor:{meu_cachorro.cor}, Idade: {meu_cachorro.idade} ")
print(f"Nome:{rex.nome}, Cor:{rex.cor}, Idade: {rex.idade} ")
print(f"Nome:{selena.nome}, Cor:{selena.cor}, Idade: {selena.idade} ")

meu_cachorro.latir("Miau") #chama o método (função) latir pelo parametro
selena.latir("Miau")
rex.latir("Miau")