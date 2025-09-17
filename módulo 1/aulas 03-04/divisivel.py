num = int(input("Digite um número inteiro: "))
resultado = num / 5
n_div = num % 5
if num % 5 == 0:
    print(F"Seu número é divisível por 5. Resultado:{resultado: .1f}")
else: 
    print(F"Seu número não é divisível. Resultado:{resultado: .1f} e Resto:{n_div: .1f} ")


