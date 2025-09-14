def contar_palavras(frase):
    return len(frase.split())

def contar_vogais(frase):
    vogais = "aeiou"
    contador = 0
    for letra in frase.lower():
        if letra in vogais:
            contador += 1
    return contador

def contar_consoantes(frase):
    vogais = "aeiou"
    contador = 0
    for letra in frase.lower():
        if letra.isalpha() and letra not in vogais:
            contador += 1
    return contador

def palindromo(frase):
    frase_limpa = ""
    for letra in frase.lower():
        if letra.isalpha():
            frase_limpa += letra
    return frase_limpa == frase_limpa[::-1]

print("𐔌 . ⋮ Analisador de Frases .ᐟ ֹ ₊ ꒱\n")
frase = input("Digite uma frase para analisar: ")

while True:
    print("𐔌 . ⋮ Resumo da Análise .ᐟ ֹ ₊ ꒱")
    print(f"Palavras: {contar_palavras(frase)}")
    print(f"Vogais: {contar_vogais(frase)}")
    print(f"Consoantes: {contar_consoantes(frase)}")
    print(f"É um palíndromo? {'Sim' if palindromo(frase) else 'Não'}")
    opçao = input("Deseja analisar outra frase? (s/n): ").lower()
    if opçao == 's':
        frase = input("Digite uma nova frase para analisar: ")
    elif opçao == 'n':
        print("𐔌 . ⋮ Obrigada por usar o analisador de frases! .ᐟ ֹ ₊ ")
        break
