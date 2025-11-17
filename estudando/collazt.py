def collatz(numero):
    while numero != 1:
        print(numero, end=" -> ")
        if numero % 2 == 0:
            numero = numero // 2
        else:
            numero = 3 * numero + 1
        
        

def passaos_collatz(numero):
    passos = 0
    while numero != 1:
        if numero % 2 == 0:
            numero = numero // 2

        else:
            numero = 3 * numero + 1
            passos += 1
    return passos

num = int(input("Digite um numero inteiro "))
print(collatz(num))
print("Quantidaade de passos:", (passaos_collatz(num)))
