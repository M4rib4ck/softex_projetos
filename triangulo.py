'''
As Regras do Jogo
1- Teste se a entrada de dados é um número.
2- Se for um número teste se é positivo
3- Para que três lados (lA,lB,lC) formem um triângulo, eles devem obedecer a duas condições importantes:
    lA<lB+lC
    lB<lA+lC
    lC<lA+lB
    ///
'''
lados = []
for i in range(1,4):
    while True:
        lado = input(f"Digite o valor do lado {i}º lado do triângulo: ")
        if lado.isdigit():
            lado = int(lado)
            if lado > 0:
                lados.append(lado)
                break
            else:
                print("Lado inválido! Deve ser um número positivo.")

l1, l2, l3 = lados
if (l1 < l2 + l3 and l1 > abs(l2 - l3) and
    l2 < l1 + l3 and l2 > abs(l1 - l3) and
    l3 < l1 + l2 and l3 > abs(l1 - l2)):
    print("Os lados podem formar um triângulo!")
else:
    print("Os lados NÃO podem formar um triângulo.")