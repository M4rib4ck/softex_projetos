
valor_x = 20.00
desconto = "tocomfome"

while True:
    lanche = input("Qual lanche você deseja? ")
    if lanche == "hamburguer":
        print("Pedido confirmado")
        break
    else:
        print("Este lanche não está cadastrado!")

cupom = input("Digite seu cupom de desconto: ")
if cupom == desconto:
    print(f"Seu lanche custou {valor_x * 0.9}")
else:
    print(f"Seu lanche custou: {valor_x}")