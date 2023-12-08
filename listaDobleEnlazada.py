from nodo import Nodo

class ListaDoble:

    def __init__(self):
        self.primero = None
        self.ultimo = None


    def insertarNodo(self, node):
        if self.primero is None:
            self.primero = self.ultimo = Nodo(node)
        else: 
            actual = self.ultimo
            self.ultimo = actual.siguiente = Nodo(node)
            self.ultimo.anterior = actual

    
    def recorrer(self):
        actual = self.primero
        while actual:
            print('Cancion: ' + actual.node.nombre)
            print('Artista: ' + actual.node.artista)
            print('Album: ' + actual.node.album)
            print('Imagen: ' + actual.node.imagen)
            print('Ruta: ' + actual.node.ruta)
            print('\n')
            actual = actual.siguiente
            