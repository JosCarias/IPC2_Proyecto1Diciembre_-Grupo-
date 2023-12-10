class Cancion:

    def __init__(self):
        self.nombre = None
        self.artista = None
        self.album = None
        self.imagen = None
        self.ruta = None

    def __str__(self) -> str:
        return "{" + str(self.nombre) + ", " + str(self.artista) + ',' + str(self.album) + ',' + str(self.imagen) + ',' + str(self.ruta) + '}'
    