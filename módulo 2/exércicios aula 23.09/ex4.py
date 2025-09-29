class Teclado:
    def __init__(self):
        pass
    def concectar_teclado(self):
        self.ligar_teclado = Teclado
        print("O teclado foi reconhecido e está pronto para uso")
    def desconectar_teclado(self):
        self.desconectar_teclado = Teclado
        print("Teclado desconectado!!")

class Mouse:
    def __init__(self):
        pass
    def concectar_mouse(self):
        self.ligar_mouse = Mouse
        print("O Mouse foi reconhecido e está pronto para uso")
    def desconectar_mouse(self):
        self.desconectar_teclado = Mouse
        print("Mouse desconectado!!")

class Monitor:
    def __init__(self):
        pass
    def conectar_monitor(self):
        self.conectar_monitor = Monitor
        print("O monitor foi reconhecido e está pronto para uso")
    def desconectar_monitor(self):
        self.desconectar_monitor = Monitor
        print("Monitor desconectado")

class Computador:
    def __init__(self):
        self.teclado = Teclado()
        self.mouse = Mouse()
        self.monitor = Monitor()
    
    def iniciar_computador(self):
        print("O computador está ligando...")
        self.teclado.concectar_teclado()
        self.mouse.concectar_mouse()
        self.monitor.conectar_monitor()
    
    def desligar_compuador(self):
        self.teclado.desconectar_teclado()
        self.mouse.desconectar_mouse()
        print("Desligando computador...")
        self.monitor.desconectar_monitor()
        print("Fora do ar")

meu_computador = Computador()
meu_computador.iniciar_computador()


        
