'''
número de telefone com 11 digitos
múmero inválido se tiver 3 ou mais digitos iguais
verificar se tem 11 caracteres e se todos são números
se o número for válido, formatar ao padrão (XX)XXXXX-XXXX
imprimir número ou mensaem de erro
'''

num = input("Digite o número com 11 digitos:" )
if not num.isdigit():
    print("Número inválido. Por favor digite apenas números.")
elif len(num) != 11:
    print("Número inválido! Deve conter 11 dígitos!")
else:
    valido = True
    for c in num:
        contador_repetido = 0
        for d in num:
            if c==d:
                contador_repetido +=1
                if contador_repetido >=3:   
                    valido = False
                    break
if not valido:
    print("Numero inválido por haver repetições")
else:
    ddd = num[:2]
    primeira = num[2:7]
    segunda = num[:7]
    formatado = f"({ddd}){primeira}-{segunda}"
    print(f"Número válido!! {formatado}")