''''
ler frase digitada pelo usuário
exibir frase codificada
descodificar a frase
print("-"*30)
letra_a = 'a'
letra_b = "b"
print(letra_a + letra_b)
'''

print("Bem vindo ao codificador de palavras!")
print("-°*'"*10)
codificada = ""
descodificado = ""

palavra = input("Digite a palavra a ser codificada: ").lower()
for letra in palavra:
    if letra == "a":
        codificada += "1"
    elif letra == "e":
        codificada += "2"
    elif letra == "i":
        codificada += "3"
    elif letra == "o":
        codificada += "4"
    elif letra == "u":
        codificada += "5"
    else:
         codificada += letra
print(f"Sua palavra codificada: {codificada}")

for letra in codificada:
    if letra == "1":
        descodificado += "a"
    elif letra == "2":
        descodificado += "e"
    elif letra == "3":
        descodificado += "i"
    elif letra == "4":
        descodificado += "o"
    elif letra == "5":
        descodificado += "u"
    else:
        descodificado += letra
print(f"Sua palavra descodificada: {descodificado}")
    