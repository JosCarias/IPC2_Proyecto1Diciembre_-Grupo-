import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

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

# funcion para buscar el archivo usando windows
def open_file_dialog():
    file_path = filedialog.askopenfilename()
    print("Archivo seleccionado:", file_path)

# boton para cargar el archivo 
btnArchivo = tk.Button(frame, text="Abrir Archivo",font="arial", command=open_file_dialog)
btnArchivo.grid(column=0,row=0,padx=5,pady=5)

#boton para generar el reporte 
btnReporte = tk.Button(frame, text="Reporte",font="arial", command="LLamar a la funcion reporte")
btnReporte.grid(column=1,row=0,padx=5,pady=5)

#textbox para buscar
txtBuscar = tk.Text(frame, width=57, height=2)
txtBuscar.grid(column=3,row=0,padx=5,pady=5)

#carga la ruta de la imagen de adelante
buscarImagen = 'Imgenes/buscar.png'
img = Image.open(buscarImagen) 
buscar = ImageTk.PhotoImage(img)

#boton para generar el buscar
btnBuscar = tk.Button(frame, image=buscar,text="Reporte",font="arial", command="LLamar a la funcion buscar")
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

#crea el boton de play
btnPlay = tk.Button(frameReproductor,image=play,font="arial", command="LLamar a la funcion play", width=60,height=60,)
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
txtBuscar = tk.Text(frameReproductor, width=45, height=10, state='disabled')
txtBuscar.grid(column=1,columnspan=5,row=1,rowspan=3,padx=10,pady=5)

#carga la ruta de la imagen de atras
atrasImagen = 'Imgenes/atras.png'
img = Image.open(atrasImagen) 
atras = ImageTk.PhotoImage(img)

#crea el boton de detener
btnAtras = tk.Button(frameReproductor,image=atras,font="arial", command="LLamar a la funcion detener", width=60,height=60)
btnAtras.grid(column=2,row=4,padx=2,pady=2)

#carga la ruta de la imagen de aleatorio
aleatorioImagen = 'Imgenes/aleatorio.png'
img = Image.open(aleatorioImagen) 
aleatorio = ImageTk.PhotoImage(img)

#crea el boton de detener
btnAtras = tk.Button(frameReproductor,image=aleatorio,font="arial", command="LLamar a la funcion detener", width=60,height=60)
btnAtras.grid(column=3,row=4,padx=2,pady=2)

#carga la ruta de la imagen de adelante
adelanteImagen = 'Imgenes/adelante.png'
img = Image.open(adelanteImagen) 
adelante = ImageTk.PhotoImage(img)

#crea el boton de adelante
btnAdelante = tk.Button(frameReproductor,image=adelante,font="arial", command="LLamar a la funcion detener", width=60,height=60)
btnAdelante.grid(column=4,row=4,padx=2,pady=2)

# Mostrar la menu
menu.mainloop()