valor = float(input("Digite o seu valor em reais: "))
if valor > 100:
    desconto = valor  * 0.10
    novo_valor = valor - desconto
    print(F"O valor com 10% de desconto({desconto: .2f}) é:{novo_valor: .2f}")
else:
    print(F"Preço sem desconto: {valor: .2f}")