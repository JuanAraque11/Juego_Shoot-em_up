import tkinter as tk

# Función para inicializar el juego
def iniciar_juego():
    pass  # Aquí añadiremos la lógica para iniciar el juego

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Buscaminas")

# Etiqueta de título
etiqueta_titulo = tk.Label(ventana, text="¡Bienvenido a Buscaminas!")
etiqueta_titulo.pack()

# Botón para iniciar el juego
boton_iniciar = tk.Button(ventana, text="Iniciar juego", command=iniciar_juego)
boton_iniciar.pack()

# Ejecutar el bucle principal
ventana.mainloop()
