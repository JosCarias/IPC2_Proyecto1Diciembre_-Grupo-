import os
from string import Template
from LecturaXml import *

def reporte_HTML():
    if lista_canciones.verificador()==True:
        cantidadCanciones = int(lista_canciones.cantidadElementos())
        if cantidadCanciones > 0:
            for i in range(cantidadCanciones):
                nombreLista = "Biblioteca"
                reproducido = lista_canciones.BuscarPorIndice(i).CantidadReproducciones
                if int(reproducido > 0):
                    nombreCancion = lista_canciones.BuscarPorIndice(i).nombre
                    nombreArtista = lista_canciones.BuscarPorIndice(i).artista
                    nombreAlbum = lista_canciones.BuscarPorIndice(i).album
                    cargarDatos(nombreLista, nombreCancion, nombreArtista, nombreAlbum, reproducido)
                i+=1
    if lista_playlists.verificador() == True:    
        numeroListas = int(lista_playlists.cantidadElementos())
        if numeroListas > 0:
            for i in range(numeroListas):
                if lista_playlists.BuscarPorIndice(i).canciones.verificador() == True:
                    numeroCanciones = int(lista_playlists.BuscarPorIndice(i).canciones.cantidadElementos())
                    if numeroCanciones > 0:
                        for j in range(numeroCanciones):
                            reproducido = cancionPorPosicionEnLista(i,j).CantidadReproducciones
                            if int(reproducido) > 0:
                                nombreLista = ver_Nombe_Lista_Posicion(i)
                                nombreCancion = cancionPorPosicionEnLista(i,j).nombre
                                nombreArtista = cancionPorPosicionEnLista(i,j).artista
                                nombreAlbum = cancionPorPosicionEnLista(i,j).album
                                cargarDatos(nombreLista, nombreCancion, nombreArtista, nombreAlbum, reproducido)
                            j+=1
                i+=1
                    


def cargarDatos(nombreLista, nombreCancion, nombreArtista, nombreAlbum, reproducido):
    archivo = open("FormatoHTML\\formato.html")

    src = Template(archivo.read()) 

    cancion = {'nombreLista':nombreLista, 'nombreCancion':nombreCancion, 'nombreArtista':nombreArtista, 'nombreAlbum':nombreAlbum,'reproducido':reproducido,}

    result = src.substitute(cancion)

    try:
        os.mkdir('Cancion')
        archivo2 = open("Reporte.html",'a')
        archivo2.writelines(result)
    except OSError:
        if os.path.exists('Cancion'):
            archivo2 = open("Reporte.html",'a')
            archivo2.writelines(result)

    os.system(r"")

if __name__=="__main__":
    reporte_HTML()

