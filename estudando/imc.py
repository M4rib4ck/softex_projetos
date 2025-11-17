def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= imc < 24.9:
        print("Peso normal")    
    elif 25 <= imc < 29.9:
        print("Sobrepeso")  
    elif 30 <= imc < 34.9:
        print("Obesidade grau 1")
    return imc
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))  
imc_calculado = calcular_imc(peso, altura)
print(f"Seu IMC é: {imc_calculado:.2f}")

