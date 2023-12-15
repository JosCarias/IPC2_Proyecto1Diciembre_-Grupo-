import xml.etree.ElementTree as ET
from listaDobleEnlazada import ListaDoble
from cancion import Cancion
from playlist import Playlist

lista_canciones = ListaDoble()
lista_album = ListaDoble()
lista_artista = ListaDoble()
lista_playlists = ListaDoble()

def Lectura_xml(ruta):
    raiz = ET.parse(ruta).getroot()

    
    for canciones in raiz.findall('cancion'):    

        nuevaCancion = Cancion()

        nombreCancion = canciones.get('nombre')
        nuevaCancion.nombre = nombreCancion

        for artistaCancion in canciones.findall('artista'):
            artista = artistaCancion.text
            nuevaCancion.artista = artista

        for albumCancion in canciones.findall('album'):
            album = albumCancion.text
            nuevaCancion.album = album

        for imagenCancion in canciones.findall('imagen'):
            imagen = imagenCancion.text
            nuevaCancion.imagen = imagen
            
        for rutaCancion in canciones.findall('ruta'):
            ruta = rutaCancion.text
            nuevaCancion.ruta = ruta
                   
        lista_canciones.insertarNodo(nuevaCancion)

def Menu():
    print("==========Proyecto1_IPC_2=========="
          +"\n\t1. Cargar archivo xml"
          +"\n\t2. Ver todas las canciones"      
          +"\n\t3. Clasificar por album"
          +"\n\t4. Clasificar por artistas"
          +"\n\t5. Salir")

def ImprimirCanciones():
    lista_canciones.recorrer() #Imprime la lista enlazada
    

def ImprimirPorAlbum(album):
    if lista_canciones.cantidadElementos()!=0:
        if lista_canciones.BuscarPorAlbum(album):
            for i in range(lista_canciones.cantidadElementos()):
                if album == lista_canciones.BuscarPorIndice(i).album:
                    lista_album.insertarNodo(lista_canciones.BuscarPorIndice(i))
                i = i + 1
            print()
            lista_album.recorrer()
        else:
            print("El album ingresado no existe")
    else:
        print("No hay elementos en la lista")

def ImprimirPorArtista(artista):
    if lista_canciones.cantidadElementos()!=0:
        if lista_canciones.BuscarPorArtista(artista):
            for i in range(lista_canciones.cantidadElementos()):
                if artista == lista_canciones.BuscarPorIndice(i).artista:
                    lista_artista.insertarNodo(lista_canciones.BuscarPorIndice(i))
                i = i + 1
            print()
            lista_artista.recorrer()
        else:
            print("El artista ingresado no existe")
    else:
        print("No hay elementos en la lista")


def Buscar_Cancion(cancion_buscada):
    cancion = lista_canciones.buscarCancion(cancion_buscada)
    print('Cancion: ' + cancion.nombre)
    print('Artista: ' + cancion.artista)
    print('Album: ' + cancion.album)
    print('Imagen: ' + cancion.imagen)
    print('Ruta: ' + cancion.ruta)
    print('\n')


def crear_playlist(nombre):
    nueva_playlist = Playlist()
    nueva_playlist.nombre = nombre
    cancion = input('Ingrese el nombre de la cancion que desea agregar a la playlist')
    cancion_encontrada = Buscar_Cancion(cancion)
    nueva_playlist.canciones.insertarNodo(cancion_encontrada)
    


if __name__ == "__main__":
    leer_xml = Lectura_xml("Entrada.xml")
    
