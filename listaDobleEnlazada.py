from nodo import Nodo

class ListaDoble:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.Cursor = None


    def insertarNodo(self, node):
        if self.primero is None:
            self.primero = self.ultimo = self.Cursor = Nodo(node)
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

    def siguienteCancion(self):
        if self.Cursor != None and self.Cursor.siguiente != None:
            self.Cursor = self.Cursor.siguiente
            return self.Cursor.node.nombre
        elif self.Cursor != None and self.Cursor.siguiente == None:
            self.Cursor = self.Cursor
            return self.Cursor.node.nombre

    def anteriorCancion(self):
        if self.Cursor != None and self.Cursor.anterior != None:
            self.Cursor = self.Cursor.anterior
            return self.Cursor.node.nombre
        elif self.Cursor != None and self.Cursor.anterior == None:
            self.Cursor = self.Cursor
            return self.Cursor.node.nombre