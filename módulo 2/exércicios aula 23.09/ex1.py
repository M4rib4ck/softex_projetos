class Motor:
    def ligar_motor(self):
        print("O motor ligou!")

    def desligar_motor(self):
        print("Desligando motor...")

class Carro:
    def __init__(self):
        self.motor = Motor()
    
    def ligar(self):
        print("O carro está ligando...")
        self.motor.ligar_motor()
        print("Carro pronto para uso")

meu_carro = Carro()
meu_carro.ligar()