from listaDobleEnlazada import ListaDoble

class Playlist:

    def __init__(self):
        self.nombre = None
        self.canciones = ListaDoble()

    def __str__(self) -> str:
        aux = self.canciones.primero
        cancion = '\n'
        while aux:
            cancion += str(aux.node) + '\n'
            aux = aux.siguiente

        return "{" + str(self.nombre) + ", "  + cancion +  '}'