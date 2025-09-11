clientes = [
    {"Nome": "Ana", "idade": 25, "cidade": "São Paulo"},
    {"Nome": "Bruno", "idade": 30, "cidade": "Rio de Janeiro"},
    {"Nome": "Carlos", "idade": 25, "cidade": "São Paulo"},
    {"Nome": "Diana", "idade": 45, "cidade": "Belo Horizonte"},
    {"Nome": "Eduarda", "idade": 30, "cidade": "Rio de Janeiro"},
    {"Nome": "Fábio", "idade": 25, "cidade": "São Paulo"}
]

print("𐔌 . ⋮ CLIENTES .ᐟ ֹ ₊ ꒱\n")
for cliente in clientes:
    nome = cliente["Nome"]
    idade = cliente["idade"]
    print(f"Nome: {nome}, idade: {idade}")

soma_idades = 0
total_clientes = 0

for cliente in clientes:
    soma_idades += cliente["idade"]

total_clientes = len(clientes)
idade_media = soma_idades / total_clientes

print("𐔌 . ⋮ IDADE MÉDIA .ᐟ ֹ ₊ ꒱")
print(f"Média: {idade_media} anos")

clientes_cidade = {}

for cliente in clientes:
    cidade = cliente["cidade"]
    if cidade in clientes_cidade:
        clientes_cidade[cidade] += 1
    else:
        clientes_cidade[cidade] = 1

    print("𐔌 . ⋮ CLIENTES POR CIDADE .ᐟ ֹ ₊ ꒱")
    print(f": {clientes_cidade}")

