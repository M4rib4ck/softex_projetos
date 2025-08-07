num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O primeiro número({num1: .1f}) é maior que o segundo número({num2: .1f})")
elif num2 > num1: 
     print(f"O segundo número({num2: .1f}) é maior que o primeiro número({num1: .1f})")
else:
     print("Os números são iguais")