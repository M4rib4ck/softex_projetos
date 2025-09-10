def banco() -> dict: #
    return {
        "usuarios":{
            "123456-7":{
                "senha": "9999",
                "nome": "José",
                "saldo": "1500,00",
                "limite_cheque_e": 500.00,
            },
        },
        "tentativas_login":3,
        "ultima_conta_base": "123456",
        "digito_verificador": "7"
    }

def autenticar_usuario(
        dados_banco: dict,
        conta: str,
        senha:str,) -> tuple[bool, dict | None]:

    usuario_encontrado = dados_banco["usuario"].get(conta, None) #nome = a nada
    if usuario_encontrado and usuario_encontrado["senha"]== senha:
        return True, usuario_encontrado
    
    return False, None

def verificar_saldo(usuario:dict) -> None:
    print(f"Seu saldo atual é: {usuario["saldo"]:.2f}")
    print(f"Seu limite de cheque especial é: {usuario["limite_cheque_e"]:.2f}")