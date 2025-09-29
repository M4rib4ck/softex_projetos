class Grao:
    def moer(self):
        print("Os grãos estão sendo moídos")
    
class Agua:
    def __init__(self):
        pass
    def aquecer_agua(self):
        print("A água está sendo aquecida")

class Cafeteria:
    def __init__(self):
        self.grao = Grao()
        self.agua = Agua()

    def fazer_cafe(self):
        print("O café está sendo feito!")
        self.grao.moer()
        self.agua.aquecer_agua()
        print("Café pronto!!")

meu_cafe = Cafeteria()
meu_cafe.fazer_cafe()
