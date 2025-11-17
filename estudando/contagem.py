pares = 0
impar = 0

while True:
    n = int(input("Digite umm número ou 0 para sair:   "))
    if n == 0:
        break

    elif n % 2 == 0:
        pares += 1
    else:
        impar += 1

print(f"Números pares: {pares}")
print(f"Números ímpares: {impar}")