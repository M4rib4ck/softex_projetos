def diga_oi():
    print("Oi!!!")
diga_oi()


def saudar(nome):
    print(f"Olá, {nome}")
saudar("Maria")
saudar("Chris")

def somar(a,b):
    return a + b
total = somar(5,3)
print(total * 2)


def encontrar_par(lista):
    for numero in lista:
        if numero % 2 == 0:
            return numero
    return None

print(encontrar_par([1, 2, 3, 4, 5, 6, 7]))

def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    return "Menor de idade"
print(verificar_idade(25))
print(verificar_idade(13))


def saudar_com_idade(nome: str, idade: int):
    return f"Olá, {nome}. Você tem {idade} anos."
print(saudar_com_idade("Chris", 22))


def somar_todos_numeros(*args): #TRANSFORMA EM TUPLA
    print(args)
somar_todos_numeros(1,2)

def exibir_perfil(**info):
    for chave, valor in info.items():
        print(info)
exibir_perfil(nome="Maria", idade=30, cidade="Rio de Janeiro")

