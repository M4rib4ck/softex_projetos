conta_c = "18735149728"
senha_c = "1234"
saldo = 1000

for tentativa in range(3):
    conta = input("Digite a sua conta: ")
    senha = input("Digite a sua senha: ")
    if conta == conta_c and senha == senha_c:
        print("Acesso liberado!")
        escolha = input("Escolha 'd' para deposito e 's' para saque. ").lower()
        if escolha == 's':
            saque = int(input("Digite o valor que deseja sacar: "))
            if saque <= saldo:
                saldo -= saque
                print(f"Saque realizado com sucesso. Seu saldo atual: R${saldo}")
                print(f"Valor sacado: R${saque}")

            else:
                print("Saldo insuficiente!")
        elif escolha == 'd':
            deposito = int(input("Digite o valor que deseja depositar: "))
            if deposito > 0:
                saldo += deposito
                print(f"Saque realizado com sucesso! Seu saldo atual é: {saldo}")
            else:
                print("Valor de deposito inválido! Tente novamente!")
        else:
            print("Operação invalida. Use 's' para saque ou 'd' para deposito:   ")
        break

    else:
        print(f"Conta ou senha incorretos. Tentativas restantes: {2 - tentativa}")
else:
    print("Número de tentativas excedido. TENTE NOVAMENTE MAIS TARDE!")