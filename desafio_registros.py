registro_acesso = []
usuarios_sucesso = set()
usuarios_falha = set()

while True: #deveria usar o try
    print("𐔌 . ⋮ MENU PRINCIPAL .ᐟ ֹ ₊ ꒱\n",
          "\n",
          "1- Inserir novo acesso!\n",
          "2- Ver registros de acesso!\n",
          "3- Sair do sistema!\n")
    
    print("𐔌 . ⋮ DIGITE A OPÇÃO: .ᐟ ֹ ₊ ꒱")
    menu = input("Opção: ")

    if not menu.isdigit() or int(menu) not in [1, 2, 3]:
        print("Opção inválida. Tente novamente.\n")
        continue  #para o loop, mas n interrompe. descarta o registro pra um novo do 0

    if menu == "3":
        break

    if menu == "2":
        print("𐔌 . ⋮ REGISTROS .ᐟ ֹ ₊ ꒱")
        if not registro_acesso:
            print("Nenhum registro de acesso encontrado.\n")
        else:
            for usuario, status, duracao in registro_acesso:
                print(f"Usuário: {usuario}, Status: {status}, Duração: {duracao} minutos\n")
        
        print("Usuários com Acesso Permitido:", usuarios_sucesso)
        print("Usuários com Acesso Negado:", usuarios_falha)

        tempo = 0
        for nome, status, duracao in registro_acesso:
            if status == "sucesso":
                tempo += duracao
        print(f"Tempo total de acesso permitido: {tempo} minutos\n")
        continue

    print("𐔌 . ⋮ USUÁRIO .ᐟ ֹ ₊ ꒱")
    usuario_nome = input("Digite o nome do usuário: ").lower()
    if not usuario_nome.isalpha():
        print("Nome inválido! Deve conter apenas letras.\n")
        continue

    print("𐔌 . ⋮ STATUS .ᐟ ֹ ₊ ꒱\n",
          "\n",
          "Selecione o status:\n",
          "1- Acesso Permitido\n",
          "2- Acesso Negado\n")

    opcao = input("Opção: ")
    if not opcao.isdigit() or int(opcao) not in [1, 2]:
        print("Opção inválida! Tente novamente.\n")
        continue

    status = "sucesso" if opcao == "1" else "falha"

    if opcao == "2":
        registro = (usuario_nome, status, 0)
        registro_acesso.append(registro)
        usuarios_falha.add(usuario_nome)
        continue

    print("𐔌 . ⋮ DURAÇÃO DA SESSÃO .ᐟ ֹ ₊ ꒱")
    duracao = input("Digite a duração da sessão em minutos: ")
    if duracao.isdigit():
        duracao = int(duracao)
    else: #except valueerror (tentar usar)
        print("Duração inválida! Tente novamente.")
        continue 

    registro = (usuario_nome, status, duracao)
    registro_acesso.append(registro)
    usuarios_sucesso.add(usuario_nome)

    print("𐔌 . ⋮ REGISTROS ATUALIZADOS .ᐟ ֹ ₊ ꒱")
    for usuario, status, duracao in registro_acesso:
        print(f"Usuário: {usuario}, Status: {status}, Duração: {duracao} minutos\n")

    print("Usuários com Acesso Permitido:", usuarios_sucesso)
    print("Usuários com Acesso Negado:", usuarios_falha)
    "\n"
    tempo = 0
    for nome, status, duracao in registro_acesso:
        if status == "sucesso":
            tempo += duracao

    print(f"𐔌 . ⋮ TEMPO TOTAL DE ATIVIDADE: .ᐟ ֹ ₊ ꒱\nTempo total de acesso permitido: {tempo} minutos\n")
