idade = int(input("Digite a sua idade:"))

if idade <= 12:
    print("Você é criança!")
elif idade <= 17:
    print("Você é adolescente!")
elif idade <= 59:
    print("Você é adulto(a)!")
else:
    print("Você é idoso(a)!")