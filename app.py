from LecturaXml import *
from reporte import reporte_HTML

    
def Principal():
    Menu()
    opcion = int(input ("\nIngrese el número de la acción que desea realizar:\n"))
    while 1<= opcion and opcion <=12:        
        if opcion == 1:
            Lectura_xml("Entrada.xml")
        elif opcion == 2:
            ImprimirCanciones()
        elif opcion == 3:
            nombreAlbum = input("Ingrese el nombre del album para la clasificación:\n")
            ImprimirPorAlbum(nombreAlbum)
        elif opcion == 4:
            nombreArtista = input("Ingrese el nombre del artista para la clasificación:\n")
            ImprimirPorArtista(nombreArtista)
        elif opcion == 5:
            playlist = input('Ingrese nombre de la playlist a crear: >')
            crear_playlist(playlist)
        elif opcion == 6:
            play = input('Ingrese el nombre de la playlist: >')
            cancion = input('Ingrese el nombre de la cancion: ')
            agregar_cancion_playlist(play, cancion)
        elif opcion == 7:
            ver_playlist()
        elif opcion == 8:
            nombreCancion = input('Ingrese el nombre de la canción:\n')
            NumeroReproduccionesCancion(nombreCancion)
        elif opcion == 9:
            indice = int(input('Ingrese la posicion de la playlist a buscar:\n'))
            ver_unaLista_Posicion(indice)
        elif opcion == 10:
            indiceLista = int(input('Ingrese la posicion de la playlist a buscar:\n'))
            indiceCancion = int(input('Ingrese la posicion que ocupa la cancion en la lista:\n'))
            cancion = cancionPorPosicionEnLista(indiceLista,indiceCancion)
            print(f'Nombre: {cancion.nombre}')
            print(f'Album: {cancion.album}')
            print(f'Artista: {cancion.artista}')
            print(f'Número de reproducciones: {cancion.CantidadReproducciones}')
        elif opcion == 11:
            reporte_HTML()
        elif opcion == 12:
            escribirXML()
        elif opcion == 13:
            print("A salido del menú")
            break  
        Menu()    
        opcion = int(input ("\nIngrese el número de la acción que desea realizar:\n"))

if __name__ == "__main__":
    Principal()
