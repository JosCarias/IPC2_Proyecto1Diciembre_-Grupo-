import xml.etree.ElementTree as ET

def Lectura_xml(ruta):
    raiz = ET.parse(ruta).getroot()

    ListaCanciones = [] #Colocar listas TDA
    
    for canciones in raiz.findall('cancion'):     
        detalles = [] #Colocar lista TDA
        nombreCancion = canciones.get('nombre')
        for artistaCancion in canciones.findall('artista'):
            artista = artistaCancion.text
        for albumCancion in canciones.findall('album'):
            album = albumCancion.text
        for imagenCancion in canciones.findall('imagen'):
            imagen = imagenCancion.text
        for rutaCancion in canciones.findall('ruta'):
            ruta = rutaCancion.text
                   
        # Realizarlo con TDA
        detalles.append([artista,album,imagen,ruta])
        ListaCanciones.append([nombreCancion,detalles])

    #Imprime la lista de listas
    # [cancion, [detalles]] => [cancion, [artista, album, imagen, ruta]]
    for cancion in ListaCanciones:
        print(cancion[0])
        for detalles in cancion[1]:
            print(detalles)
        print()

if __name__ == "__main__":
    leer_xml = Lectura_xml("Entrada.xml")