import xml.etree.ElementTree as ET
from listaDobleEnlazada import ListaDoble
from cancion import Cancion

lista_canciones = ListaDoble()

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
    lista_canciones.recorrer() #Imprime la lista enlazada

    lista_canciones.siguienteCancion() # Pasa a la cancion 2
    lista_canciones.siguienteCancion() # Pasa a la cancion 3
    lista_canciones.siguienteCancion() # Pasa a la cancion 4
    lista_canciones.siguienteCancion() # Pasa a la cancion 5
    lista_canciones.siguienteCancion() # Pasa a la cancion 6
    lista_canciones.anteriorCancion() # Regresa a la cancion 5
    lista_canciones.anteriorCancion() # Regresa a la cancion 4
    lista_canciones.siguienteCancion() # Pasa a la cancion 5
    cancion = lista_canciones.siguienteCancion() # Pasa a la cancion 6
    print(f"El nombre de la canción es: {cancion}")



if __name__ == "__main__":
    leer_xml = Lectura_xml("Entrada.xml")