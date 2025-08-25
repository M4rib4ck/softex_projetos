posicao_i = 0
while True:
        print("==== Menu de opções ==== \n"\
        "1- Avançar.\n"\
        "2- Recuar.\n"\
        "3- Status.\n"\
        "4- Desligar.\n")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
           valor = int(input(" Digite a quantidade de casas que deseja avançar(<5): "))
           if valor > 0:
                posicao_i += valor
           else:
                print("Valor inválido, tente novamente.")
           print(f"O robo andou {valor} casas.")
        elif opcao == "2":
              valor = int(input("Digite a quantidade de casas que deseja recuar(<5): "))
              if valor > 0:
                   posicao_i -= valor
                   print(f"O robo andou {valor} casas.")
              else:
                   print("Valor inválido, tente novamente.") 
        elif opcao == "3":
              print(f"O robo está na posição: {posicao_i}")
        elif opcao == "4":
              print("Encerrando sistema do robo...")
              break
        else: 
              print("Comando inválido!!")