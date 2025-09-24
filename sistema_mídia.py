class Midia:
    def __init__(self, titulo, duracao_seg):
        self.titulo = titulo
        self.duracao_seg = duracao_seg
    def exibir(self):
        print(f"{self.titulo} duração: {self.duracao_seg}seg")

class Musica(Midia):
    def __init__(self, titulo, duracao_seg, artista):
        super().__init__(titulo, duracao_seg)
        self.artista = artista

    def __str__(self):
        return self.titulo
    
    def exibir(self):
        print(f"Dados da música: {self.titulo} duração: {self.duracao_seg}seg, artista: {self.artista}")
   
musica1= Musica("Bigmouth strikes again", 3.13, "The Smiths")
musica2 = Musica("Holy Diver", 5.40, "DIO")

lista_musicas = [musica1, musica2]
for Musica in lista_musicas:
    Musica.exibir()

class Video(Midia):
    def __init__(self, titulo, duracao_seg, resolucao):
        super().__init__(titulo, duracao_seg)
        self.resolucao = resolucao

    def exibir(self):
        print(f"Dados do seu vídeo: {self.titulo} duração: {self.duracao_seg}seg, resolução: {self.resolucao}")

    def __str__(self):
        return self.titulo

video1 = Video("Para onde ir em Hollow Knight", 6.56, "1920x1080")
print(video1)
lista_video= [video1]
for Videos in lista_video:
    Videos.exibir()
