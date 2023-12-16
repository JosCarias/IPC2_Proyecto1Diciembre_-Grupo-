import os
from string import Template
from LecturaXml import *

def reporte_HTML():    
    numeroListas = int(lista_playlists.cantidadElementos())
    if numeroListas > 0:
        for i in range(numeroListas):
            numeroCanciones = int(lista_playlists.BuscarPorIndice(i).canciones.cantidadElementos())
            if numeroCanciones > 0:
                for j in range(numeroCanciones):
                    nombreLista = ver_Nombe_Lista_Posicion(i)
                    nombreCancion = cancionPorPosicionEnLista(i,j).nombre
                    nombreArtista = cancionPorPosicionEnLista(i,j).artista
                    nombreAlbum = cancionPorPosicionEnLista(i,j).album
                    reproducido = cancionPorPosicionEnLista(i,j).CantidadReproducciones
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

