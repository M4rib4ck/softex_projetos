while True:
    try:
        idade = int(input("Digite a idade: "))
        break
    except ValueError:
        print("Por favor, insira um número válido para a idade.")

def classificar_idade(idade):
    if idade < 0:
        return "𐔌 . ⋮ Idade inválida .ᐟ ֹ ₊ ꒱"
    elif idade <= 12:
        return "𐔌 . ⋮ Criança .ᐟ ֹ ₊ ꒱"
    elif idade <= 19:
        return "𐔌 . ⋮ Adolescente .ᐟ ֹ ₊ ꒱"
    elif idade <= 59:
        return "𐔌 . ⋮ Adulto .ᐟ ֹ ₊ ꒱"
    else:
        return "𐔌 . ⋮ Idoso .ᐟ ֹ ₊ ꒱"
resultado = classificar_idade(idade)
print("A idade digitada é de um(a):"), print(resultado)