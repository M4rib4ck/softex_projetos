nome = input("Qual é o seu nome? ")
idade = float(input("Qual é a sua idade? "))


if idade >= 18:
    print(f"Olá, {nome}, você tem {idade: .1f} anos e é maior de idade")
else:
    print(f"Olá, {nome}, você tem {idade: .1f} anos e é menor de idade")