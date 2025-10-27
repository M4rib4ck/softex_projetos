def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def processar_lista(lista):
    if not lista:
        raise ValueError("Lista não pode ser vazia.")
    return sorted(lista)

def buscar_usuario(usuarios: list, id_usuario: int):
    for usuario in usuarios:
        if usuario.get('id') == id_usuario:
            return usuario
    return None

