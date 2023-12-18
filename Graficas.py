from graphviz import Digraph
from listaDobleEnlazada import *

from LecturaXml import *


def hacerGrafo():
    # Crear un gráfico DOT
    dot = Digraph(comment='Canciones')
    largoLista = int(lista_canciones.cantidadElementos())
    
    dot.node("TITULO", "Biblioteca")

    # Agregar nodos con forma ovalada para los nombres de las canciones
    for i in range(largoLista):
        cancion = lista_canciones.BuscarPorIndice(i)
        dot.node(str(i), str(cancion.nombre))

    # Agregar bordes entre los nodos de los nombres de las canciones
    for i in range(largoLista - 1):
        dot.edge(str(i), str(i + 1))

    # Agregar nodos con forma cuadrada para los álbumes
    for i in range(largoLista):
        cancion = lista_canciones.BuscarPorIndice(i)
        dot.node(str(largoLista + i), str(cancion.album)) 

    # Agregar bordes entre los nodos de los álbumes
    for i in range(largoLista - 1):
        dot.edge(str(largoLista + i), str(largoLista + i + 1))
        
    for i in range(largoLista):
        cancion = lista_canciones.BuscarPorIndice(i)
        dot.node(str(largoLista*2 + i), str(cancion.artista)) 
    
    for i in range(largoLista - 1):
        dot.edge(str(largoLista*2 + i), str(largoLista*2 + i + 1))
        
    dot.edge("TITULO","0")
    dot.edge("TITULO",str(largoLista*1))
    dot.edge("TITULO",str(largoLista*2))

    # Generar el archivo DOT
    dot.render('productos_grafo', format='png', view=True)