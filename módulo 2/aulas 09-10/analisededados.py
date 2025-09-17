vendas = [
    ("Base", 25, 6),
    ("Paleta de sombra", 95, 1),
    ("Kit de pinceis", 50, 2),
    ("Iluminador", 15, 7),
    ("Blush", 25, 4),
    ("Delineador", 25, 1),
    ("Rimel", 50, 1),
]

vendas_filtradas = list() #[]
produtos_unicos = set()

for produto, valor, quantidade in vendas:
    valor_total = valor * quantidade
    if valor_total >= 100:
        vendas_filtradas.append((produto, valor, quantidade))
    produtos_unicos.add(produto)

print("Vendas filtradas de valores maior que 100:")
if vendas_filtradas:
    for produto, valor, quantidade in vendas_filtradas:
        valor_total = valor * quantidade
        print(f"{produto}: {quantidade} x R${valor:.2f} = R${valor_total:.2f}")
else:
    print("Nenhuma venda atingiu R$100.")


