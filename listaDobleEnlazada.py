import random
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
        self .__unir_nodos()

    
    def recorrer(self):
        actual = self.primero
        if self.primero != None:
            while actual:
                print('Cancion: ' + actual.node.nombre)
                print('Artista: ' + actual.node.artista)
                print('Album: ' + actual.node.album)
                print('Imagen: ' + actual.node.imagen)
                print('Ruta: ' + actual.node.ruta)
                print('\n') 
                actual = actual.siguiente
                if actual == self.primero:
                    break
        else:
            print('La lista está vacía\n')
    
    def siguienteCancion(self):
        if self.Cursor and self.Cursor.siguiente:
            self.Cursor = self.Cursor.siguiente
        return self.Cursor.node 

    def anteriorCancion(self):
        if self.Cursor and self.Cursor.anterior:
            self.Cursor = self.Cursor.anterior
        return self.Cursor.node

    def aleatorioCancion(self):
        if self.Cursor:
            indice = random.randint(0, int(self.cantidadElementos())-1)
            self.Cursor = self.BuscarPorIndice(indice)
        return self.Cursor
        
    def cantidadElementos(self):
        contador = 0
        aux = self.primero
        if aux != None:
            while aux != None:
                contador = contador + 1
                aux = aux.siguiente
                if aux == self.primero:
                    return contador

    def BuscarPorIndice(self, indice):
        contador = 0
        aux = self.primero
        if aux != None:
            while aux != None:
                if contador == indice:
                    return aux.node
                else:
                    aux = aux.siguiente
                    contador = contador + 1
                    if aux == self.primero:
                        return None
        return None
    
    def BuscarPorAlbum(self, album):
        aux = self.primero
        if aux != None:
            while aux != None:
                if aux.node.album == album:
                    return True
                else:
                    aux = aux.siguiente
                    if aux == self.primero:
                        return False
        return False
    
    def BuscarPorArtista(self, artista):
        aux = self.primero
        if aux != None:
            while aux != None:
                if aux.node.artista == artista:
                    return True
                else:
                    aux = aux.siguiente
                    if aux == self.primero:
                        return False
        return False
    
    def buscarCancion(self, nombre):
        if self.primero is None:
            return
        actual = self.primero
        while actual:
            if actual.node.nombre == nombre:
                return actual.node
            else:
                actual = actual.siguiente
                if actual == self.primero:
                    return

    def __unir_nodos(self):
        if self.primero!=None:
            self.primero.anterior=self.ultimo
            self.ultimo.siguiente=self.primero