estoque_principal = [
    ("Camisa", 100),
    ("Calça", 101),
    ("Boné", 102),
    ("Têmis", 103),
]
estoque_online = [
    ("Boné", 102),
    ("Camisa polo", 105),
    ("Calça", 101),
    ("Chinelo", 106)
]

set_principal = set(estoque_principal)
set_online = set(estoque_online)

em_ambos = set_principal.intersection(set_online)
print("Produtos disponíveis na loja e no site: ")
print(em_ambos)

apenas_loja = set_principal.difference(set_online)
print("Produtos disponíveis apenas na loja: ")
print(apenas_loja)

apenas_online = set_online.difference(set_principal)
print("Produtos disponíveis apenas no site: ")
print(apenas_online)