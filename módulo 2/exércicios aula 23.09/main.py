from nomes import Pessoas

lista_de_pessoas = []

while True:
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")

    pessoa = Pessoas(nome, idade)
    lista_de_pessoas.append(pessoa)

    opção = input("Deseja adicionar outra pessoa? (sim/não): ").strip().lower()
    if opção != "sim":
        break

print("Pessoas cadastradas:")
for p in lista_de_pessoas:
    print(p) 