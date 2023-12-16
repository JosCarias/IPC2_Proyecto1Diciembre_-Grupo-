import os
from string import Template
from LecturaXml import *

def reporte_HTML():
    archivo = open("FormatoHTML\\formato.html")

    src = Template(archivo.read())

    nombreLista = ver_Nombe_Lista_Posicion(0)
    nombreCancion = cancionPorPosicionEnLista(0,0).nombre
    nombreArtista = cancionPorPosicionEnLista(0,0).artista
    nombreAlbum = cancionPorPosicionEnLista(0,0).album
    reproducido = cancionPorPosicionEnLista(0,0).CantidadReproducciones

    # nombreLista = "Lista 1"
    # nombreCancion = "Graveyar" 
    # nombreArtista = "Cantante 1"
    # nombreAlbum = "Sencillo" 
    # reproducido = "1" 


    cancion = {'nombreLista':nombreLista, 'nombreCancion':nombreCancion, 'nombreArtista':nombreArtista, 'nombreAlbum':nombreAlbum,'reproducido':reproducido,}

    result = src.substitute(cancion)

    try:
        os.mkdir('Cancion')
        archivo2 = open("Reporte.html",'a')
        archivo2.writelines(result)
        print('Guardado')
    except OSError:
        if os.path.exists('Cancion'):
            archivo2 = open("Reporte.html",'a')
            archivo2.writelines(result)
            print('Guardado')

    os.system(r"")

if __name__=="__main__":
    reporte_HTML()

