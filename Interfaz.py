import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from LecturaXml import *

def menuPrincipal():
    # Crear la menu principal
    menu = tk.Tk()

    # Establecer título y tamaño de la menu
    menu.title("IPCMusic ")
    menu.geometry("720x480") 
    menu.resizable(False, False) 
    menu.config(bg="gray")

    # frame donde estan los botones y la barra de busqueda
    frame = tk.Frame(menu, width=700, height=50, bg="lightgrey")
    frame.grid(column=0,row=0,padx=10, pady=10,)

    # boton para cargar el archivo 
    btnArchivo = tk.Button(frame, text="Archivo",font="arial", command=menuSecundario)
    btnArchivo.grid(column=0,row=0,padx=5,pady=5)

    #boton para generar el reporte 
    btnReporte = tk.Button(frame, text="Reporte",font="arial", command="LLamar a la funcion reporte")
    btnReporte.grid(column=1,row=0,padx=5,pady=5)

    #textbox para buscar
    txtBarra = tk.Text(frame, width=57, height=2)
    txtBarra.grid(column=3,row=0,padx=5,pady=5)

    #carga la ruta de la imagen de adelante
    buscarImagen = 'Imgenes/buscar.png'
    img = Image.open(buscarImagen) 
    buscar = ImageTk.PhotoImage(img)

    #Funcion para buscar cancion por nombre
    def buscarPorCancion():
        txtBuscar.delete('1.0', tk.END)
        txtBuscar.insert(tk.END, (formatoBuscarCancion(txtBarra.get("1.0", "end-1c"))))

    #funcion encargada de dar formato a la informacion de salida      
    def formatoBuscarCancion(nombre):
        datos=lista_canciones.buscarCancion(nombre)
        salida="Nombre: "+datos.nombre+"\n"
        salida+="Artista: "+datos.artista+"\n"
        salida+="Album: "+datos.album+"\n"
        return salida


    #boton para generar el buscar
    btnBuscar = tk.Button(frame, image=buscar,text="Reporte",font="arial", command=buscarPorCancion)
    btnBuscar.grid(column=4,row=0,padx=5,pady=5)

    #frame de abajo, contiene las imagnes y los botones
    frameReproductor = tk.Frame(menu, width=800, height=100, bg="lightgrey")
    frameReproductor.grid(column=0,row=1,padx=10)

    #carga la ruta de la imagen 
    albunImagen = 'Imgenes\defaulAlbumPequeño.png'
    img = Image.open(albunImagen)
    Album = ImageTk.PhotoImage(img)

    #es la imagen del album
    label = tk.Label(frameReproductor, image=Album, height=250,width=250)
    label.grid(column=0,rowspan=5,row=0,padx=10,pady=10)

    #carga la ruta de la imagen de play
    playImagen = 'Imgenes\playPequeño.png'
    img = Image.open(playImagen) 
    play = ImageTk.PhotoImage(img)
    
    #Funcion para dar formato a la infomacion
    def textoDeInformacion():
        dato=lista_canciones.BuscarPorIndice(0)
        salida="Nombre: "+dato.nombre+"\n"
        salida+="Artista: "+dato.artista+"\n"
        salida+="Album: "+dato.album+"\n"
        txtBuscar.delete('1.0', tk.END)
        txtBuscar.insert(tk.END, (str(salida)))
        

    #crea el boton de play
    btnPlay = tk.Button(frameReproductor,image=play,font="arial", command=textoDeInformacion, width=60,height=60,)
    btnPlay.grid(column=2,row=0,padx=2,pady=2)

    #carga la ruta de la imagen de pausa
    pauseImagen = 'Imgenes\pausaPequeño.png'
    img = Image.open(pauseImagen) 
    pause = ImageTk.PhotoImage(img)

    #crea el boton de pausa
    btnPausa = tk.Button(frameReproductor,image=pause,font="arial", command="LLamar a la funcion pausa", width=60,height=60)
    btnPausa.grid(column=3,row=0,padx=2,pady=2)

    #carga la ruta de la imagen de detener
    detenerImagen = 'Imgenes\detenerPqueño.png'
    img = Image.open(detenerImagen) 
    detener = ImageTk.PhotoImage(img)

    #crea el boton de detener
    btnDetener = tk.Button(frameReproductor,image=detener,font="arial", command="LLamar a la funcion detener", width=60,height=60)
    btnDetener.grid(column=4,row=0,padx=2,pady=2)

    #textbox para informacion
    txtBuscar = tk.Text(frameReproductor, width=45, height=10)
    txtBuscar.grid(column=1,columnspan=5,row=1,rowspan=3,padx=10,pady=5)

    #carga la ruta de la imagen de atras
    atrasImagen = 'Imgenes/atras.png'
    img = Image.open(atrasImagen) 
    atras = ImageTk.PhotoImage(img)

    #Funcion para adelantar cancion
    def atrasarCancion():
        txtBuscar.delete('1.0', tk.END)
        txtBuscar.insert(tk.END, (str(formatoAtrasar())))

    #funcion encargada de dar formato a la informacion de salida      
    def formatoAtrasar():
        datos=lista_canciones.anteriorCancion()
        salida="Nombre: "+datos.nombre+"\n"
        salida+="Artista: "+datos.artista+"\n"
        salida+="Album: "+datos.album+"\n"
        return salida    

    #crea el boton de atras
    btnAtras = tk.Button(frameReproductor,image=atras,font="arial", command=atrasarCancion, width=60,height=60)
    btnAtras.grid(column=2,row=4,padx=2,pady=2)

    #carga la ruta de la imagen de aleatorio
    aleatorioImagen = 'Imgenes/aleatorio.png'
    img = Image.open(aleatorioImagen) 
    aleatorio = ImageTk.PhotoImage(img)


    #Funcion para cancion aleatoria
    def cancionAleatoria():
        txtBuscar.delete('1.0', tk.END)
        lista_canciones.aleatorioCancion()
        txtBuscar.insert(tk.END, (str("Se ha activado el modo aleatorio")))         

    #crea el boton de aleatorio
    btnAleatorio = tk.Button(frameReproductor,image=aleatorio,font="arial", command=cancionAleatoria, width=60,height=60)
    btnAleatorio.grid(column=3,row=4,padx=2,pady=2)

    #carga la ruta de la imagen de adelante
    adelanteImagen = 'Imgenes/adelante.png'
    img = Image.open(adelanteImagen) 
    adelante = ImageTk.PhotoImage(img)

    #Funcion para adelantar cancion
    def adelantarCancion():
        txtBuscar.delete('1.0', tk.END)
        txtBuscar.insert(tk.END, (str(formatoAdelantar())))

    #funcion encargada de dar formato a la informacion de salida  
    def formatoAdelantar():
        datos=lista_canciones.siguienteCancion()
        salida="Nombre: "+datos.nombre+"\n"
        salida+="Artista: "+datos.artista+"\n"
        salida+="Album: "+datos.album+"\n"
        return salida

    #crea el boton de adelante
    btnAdelante = tk.Button(frameReproductor,image=adelante,font="arial", command=adelantarCancion, width=60,height=60)
    btnAdelante.grid(column=4,row=4,padx=2,pady=2)


    # Mostrar la menu
    menu.mainloop()
    
def menuSecundario():
    menu = tk.Tk()

    # Establecer título y tamaño de la menu
    menu.title("IPCMusic ")
    menu.geometry("720x480") 
    menu.resizable(False, False) 
    menu.config(bg="gray")

    frameDeArriba = tk.Frame(menu, width=700, height=50, bg="lightgrey")
    frameDeArriba.grid(padx=10, pady=10)
    
    # funcion para buscar el archivo usando windows
    def open_file_dialog():
        archivo = filedialog.askopenfile(filetypes=[("Archivos de texto", "*.xml"), ("Todos los archivos", "*.*")])

        if archivo:
            ruta=archivo.name 
            Lectura_xml(ruta)
            lista_canciones.recorrer()
    
    # boton para cargar el archivo 
    btnArchivo = tk.Button(frameDeArriba, text="Abrir Archivo",font="arial", command=open_file_dialog)
    btnArchivo.grid(column=0,row=0,padx=5,pady=5)
    
    # boton para ver Playlist
    btnArchivo = tk.Button(frameDeArriba, text="Ver Playlists",font="arial", command="")
    btnArchivo.grid(column=1,row=0,padx=5,pady=5)
    
    #frame de abajo, contiene las imagnes y los botones
    frameReproductor = tk.Frame(menu, width=700, height=100, bg="lightgrey")
    frameReproductor.grid(column=0,row=1,padx=10)
    
    labelNombreLista=tk.Label(frameReproductor,text="Ingrese el nombre de la playList", bg="lightgrey")
    labelNombreLista.grid(column=3,row=0,padx=5,pady=5)
    
    #textbox para buscar
    txtBarra = tk.Text(frameReproductor, width=40, height=2)
    txtBarra.grid(column=4,row=0,padx=5,pady=5) 
    
    #textbox para informacion
    txtBuscar = tk.Text(frameReproductor, width=80, height=5)
    txtBuscar.grid(column=0,columnspan=5,row=1,rowspan=3,padx=10,pady=10)
    
    #crea el boton de adelante
    btnCrar = tk.Button(frameReproductor,text="Crear playlist",font="arial")
    btnCrar.grid(column=4,row=4,padx=2,pady=2)
    
    #frame de abajo, contiene las imagnes y los botones
    frameMegusta = tk.Frame(menu, width=700, height=100, bg="lightgrey")
    frameMegusta.grid(column=0,row=2,padx=10,pady=5)
    
    #textbox para buscar
    txtBarra = tk.Text(frameMegusta, width=40, height=2)
    txtBarra.grid(column=4,row=0,padx=5,pady=5)

    #boton para generar el buscar
    btnBuscar = tk.Button(frameMegusta, text="Buscar Cancion", font="Arial")
    btnBuscar.grid(column=3, row=0, padx=5, pady=5) 
    
    #textbox para informacion
    txtBuscar = tk.Text(frameMegusta, width=80, height=5)
    txtBuscar.grid(column=0,columnspan=5,row=1,rowspan=3,padx=10,pady=10)
    
    #crea el boton de adelante
    btnAgregar = tk.Button(frameMegusta,text="Agregar Cancion",font="arial")
    btnAgregar.grid(column=4,row=5,padx=2,pady=2)
    
    menu.mainloop()
       
menuPrincipal()

#menuSecundario()


