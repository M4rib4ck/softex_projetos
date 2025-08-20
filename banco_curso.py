conta_c = "123456-7"
senha_c = "030904"
saldo_a = 0
limite_saldo_n = 500.00
nome_usuario = "Maria"

while True:
    for i in range(3):
        conta = input("Entre com a sua conta corrente: ")
        senha = input("Entre com a sua senha: ")
        if conta == conta_c and  senha == senha_c:
                print(f"Bem-vindo, {nome_usuario}!!")
                acesso_permitido = True
                break
        else:
                print("Conta ou senha inválida!")
                acesso_permitido = False
    if not acesso_permitido:
        break

    while True:
        opcao = (input("Escolha uma opção: \n")\
        "1- Ver saldo.\n"\
        "2- Sacar valor.\n"\
        "3- Depositar.\n"\
        "4- Pagar boleto.\n"\
        "5- Alterar senha.\n"\
        "6- Sair.\n")
        if opcao == 1:
            print(f"Seu saldo atual é de {saldo_a}.")
        elif opcao == 2:
            valor_saque = float(input("Entre com o valor a ser sacado: "))
            if valor_saque <= (saldo_a + limite_saldo_n):
                saldo -= valor_saque
                print("Saldo liberado, retire seu valor!")
            else:
                print("Saldo insuficiente!")

        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            pass
        elif opcao == 6:
            print("Atendimento finalizado!")
            break
        else:
            pass