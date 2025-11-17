def juros (valor, taxa, tempo):
    resultado_juros = valor * (taxa / 100) * tempo
    return resultado_juros

valor_inicial =  float(input("Digite o valor inicial: "))
taxa_juros = float(input("Digite a taxa dde juros (%): "))
tempo_emprestimo = int(input("Digite o tempo em meses: "))

juros_calculado = juros(valor_inicial, taxa_juros, tempo_emprestimo)
valor_final = valor_inicial + juros_calculado

print(f"O valor dos juros é: {juros_calculado:.2f}")
print(f"O valor final após {tempo_emprestimo} meses é: {valor_final:.2f}")
