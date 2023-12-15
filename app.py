from LecturaXml import *

    
def Principal():
    Menu()
    opcion = int(input ("\nIngrese el número de la acción que desea realizar:\n"))
    while 1<= opcion and opcion <=9:        
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
            print("A salido del menú")
            break  
        Menu()    
        opcion = int(input ("\nIngrese el número de la acción que desea realizar:\n"))

if __name__ == "__main__":
    Principal()
