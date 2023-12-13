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
        if self.primero != None:
            while actual:
                print('Cancion: ' + actual.node.nombre)
                print('Artista: ' + actual.node.artista)
                print('Album: ' + actual.node.album)
                print('Imagen: ' + actual.node.imagen)
                print('Ruta: ' + actual.node.ruta)
                print('\n') 
                actual = actual.siguiente
        else:
            print('La lista está vacía\n')
    
    def siguienteCancion(self):
        if self.Cursor and self.Cursor.siguiente:
            self.Cursor = self.Cursor.siguiente
        return self.Cursor.node if self.Cursor else None

    def anteriorCancion(self):
        if self.Cursor and self.Cursor.anterior:
            self.Cursor = self.Cursor.anterior
        return self.Cursor.node if self.Cursor else None
        
    def cantidadElementos(self):
        contador = 0
        aux = self.primero
        if aux != None:
            while aux != None:
                contador = contador + 1
                aux = aux.siguiente
            return contador
        return contador

    def BuscarPorIndice(self, indice):
        contador = 0
        aux = self.primero
        if aux != None:
            while aux != None:
                if contador == indice:
                    return aux.node
                aux = aux.siguiente
                contador = contador + 1
        return None
    
    def BuscarPorAlbum(self, album):
        aux = self.primero
        if aux != None:
            while aux != None:
                if aux.node.album == album:
                    return True
                aux = aux.siguiente
        return False
    
    def BuscarPorArtista(self, artista):
        aux = self.primero
        if aux != None:
            while aux != None:
                if aux.node.artista == artista:
                    return True
                aux = aux.siguiente
        return False

    def eliminarPrimero(self):
        if self.primero != None:
            if self.primero.siguiente == None:
                Aux = self.primero
                self.primero = None
                self.Final = None
                return Aux.node
            else:
                Aux = self.primero
                self.primero = self.primero.siguiente
                self.primero.anterior = None
                Aux.siguiente = None
                return Aux.node

    def eliminarIndice(self, indice):
        if self.primero == None:
            print("La lista está vacía")
            return None
        if indice == 0:
            aux = self.eliminarPrimero()
            return aux
        if indice < 0:
            print("No existen posiciones menores que cero")
            return None
        contador = 0
        previo = None
        aux = self.primero
        while aux != None:
            if contador == indice:
                if aux == self.ultimo:
                    self.ultimo = previo
                    aux.anterior = None
                    previo.siguiente = None
                    return aux.node
                previo.siguiente=aux.siguiente
                posterior = aux.siguiente
                aux.siguiente=None
                posterior.anterior = aux.anterior
                aux.anterior=None
                return aux.node
            previo = aux
            aux = aux.siguiente
            contador += 1
        print("No existe la posición indicada")
        return None