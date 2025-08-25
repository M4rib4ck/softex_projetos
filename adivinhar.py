numero_secreto = 25
for i in range(5):
    numero = int(input("Digite um número:"))
    if numero >= 30:
        print("Muito alto, tente novamente!")
    elif numero <= 22:
        print("Muito baixo, tente novamente!")
    elif numero <= 24:
        print("Está bem próximo, tente novamente")
    elif numero == numero_secreto:
        print("!!! Você acertou !!! ")
        break

    

