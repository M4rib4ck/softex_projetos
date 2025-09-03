registros = [
    ("Pedro", "sucesso"),
    ("Ana", "falha" ),
    ("Maria", "sucesso"),
    ("Pedro", "falha"),
    ("Ana", "falha")
]

login_realizado = set()
login_recusado = set()

for usuario, status in registros:
    if status == "sucesso":
        login_realizado.add(usuario)
    elif status == "falha":
        login_recusado.add(usuario)
        
somente_falha = login_recusado.difference(login_realizado)
em_ambos = login_realizado.intersection(login_recusado)

print("\nUsuários com pelo menos um login bem-sucedido:")
print(login_realizado)
print("\nUsuários que tiveram somente logins com falha:")
print(somente_falha)
print("\nUsuários com sucesso e falha: ")
print(em_ambos)



