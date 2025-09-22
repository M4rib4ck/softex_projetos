print("𐔌 . ⋮ Bem-Vindo .ᐟ ֹ ₊ ꒱\n")

def receber_nome():
    print("Qual é o seu nome?")
    nome = input(":")
    if not nome.isalpha():
        print("Por favor, insira um nome válido. Não pode conter números ou símbolos.")
        return receber_nome()
    return nome

def receber_idade():
    while True:
        try:
            idade = int(input("Digite a sua idade: "))
            return idade
        except ValueError:
            print("Por favor, insira um número válido para a idade. Não pode conter letras ou símbolos.")
def classificar_idade(idade):
    if idade < 0 or idade > 150:
        return "𐔌 . ⋮ Idade inválida .ᐟ ֹ ₊ ꒱"
    elif idade <= 12:
        return "𐔌 . ⋮ Criança .ᐟ ֹ ₊ ꒱"
    elif idade <= 18:
        return "𐔌 . ⋮ Adolescente .ᐟ ֹ ₊ ꒱"
    elif idade <= 59:
        return "𐔌 . ⋮ Adulto .ᐟ ֹ ₊ ꒱"
    else:
        return "𐔌 . ⋮ Idoso .ᐟ ֹ ₊ ꒱"
    
def exibir_resultado(nome, idade, classificacao):
    print(f"Olá, {nome}, você tem {idade} anos e é classificado(a) como: {classificacao}")

nome = receber_nome()
idade = receber_idade()
classificacao = classificar_idade(idade)
exibir_resultado(nome, idade, classificacao)