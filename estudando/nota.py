def notas_missin(nota1, trabalho1, nota2, trabalho2):
    p1 = (nota1 * 0.8) + (trabalho1 * 0.2)
    p2 = (nota2 * 0.8) + (trabalho2 * 0.2)
    media_final = (p1 + p2) / 2
    if media_final >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
    return media_final

n1= float(input("Digite a primeira nota: "))
t1= float(input("Digite a nota do primeiro trabalho: "))
n2= float(input("Digite a segunda nota: "))     
t2= float(input("Digite a nota do segundo trabalho: "))
print(notas_missin(n1, t1, n2, t2))
