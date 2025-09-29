class Ponto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class SegmentoDeReta:
    def __init__(self, ponto1, ponto2):
        self.ponto1 = ponto1
        self.ponto2 = ponto2

    def calcular_comprimento(self):
        dx = self.ponto2.x - self.ponto1.x
        dy = self.ponto2.y - self.ponto1.y
        return(dx**2 + dy**2)


p1 = Ponto(0, 0)
p2 = Ponto(3, 4)
segmento = SegmentoDeReta(p1, p2)

print("Comprimento do segmento de reta:", segmento.calcular_comprimento())
        