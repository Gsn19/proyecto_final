import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

# Variables globales para las entradas de texto y el historial
entry_a = None
entry_b = None
historial = []
fig = None

# Función para graficar la ecuación de la recta
def graficar_recta():
    # Obtener los valores de las variables a y b desde las entradas de texto
    a = float(entry_a.get())
    b = float(entry_b.get())

    # Generar los puntos para la gráfica de la recta
    x = np.linspace(-10, 10, 100)
    y = a * x + b

    global fig
    if fig is not None:
        # Si la figura ya existe, solo actualizamos los datos de la gráfica
        lines = fig.axes[0].lines
        lines[0].set_data(x, y)
        fig.canvas.draw_idle()
    else:
        # Si la figura no existe, creamos una nueva gráfica
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Gráfica de la Recta')
        ax.grid(True)
        plt.show(block=False)

    # Agregar la ecuación y el procedimiento al historial
    ecuacion = f"y = {a}x + {b}"
    procedimiento = f"Generar puntos con x de -10 a 10 y calcular y = {a} * x + {b}"
    historial.append((ecuacion, procedimiento))

# Función para abrir el formulario ER
def abrir_form_er():
    form_er = tk.Toplevel(root)
    
    # Etiqueta y entrada de texto para el valor de "a"
    label_a = tk.Label(form_er, text="Valor de a:")
    label_a.pack()
    global entry_a
    entry_a = tk.Entry(form_er)
    entry_a.pack()

    # Etiqueta y entrada de texto para el valor de "b"
    label_b = tk.Label(form_er, text="Valor de b:")
    label_b.pack()
    global entry_b
    entry_b = tk.Entry(form_er)
    entry_b.pack()

    # Botón para graficar la ecuación de la recta
    btn_graficar = tk.Button(form_er, text="Graficar", command=graficar_recta)
    btn_graficar.pack()

# Función para abrir el historial
def abrir_historial():
    historial_window = tk.Toplevel(root)
    historial_window.title("Historial de ecuaciones y procedimientos")
    
    # Crear un widget Listbox para mostrar el historial
    listbox = tk.Listbox(historial_window, width=60, height=10)
    listbox.pack()

    # Agregar cada ecuación al Listbox
    for i, (ecuacion, _) in enumerate(historial):
        listbox.insert(tk.END, f"Ecuación {i+1}: {ecuacion}")

    # Función para volver a la ecuación seleccionada
    def volver_ecuacion():
        seleccionado = listbox.curselection()
        if seleccionado:
            indice = seleccionado[0]
            _, a, _, b = historial[indice][0].split()
            entry_a.delete(0, tk.END)
            entry_a.insert(0, a)
            entry_b.delete(0, tk.END)
            entry_b.insert(0, b)
            graficar_recta()

    # Botón para volver a la ecuación seleccionada
    btn_volver = tk.Button(historial_window, text="Volver a la ecuación", command=volver_ecuacion)
    btn_volver.pack()

# Crear ventana principal
root = tk.Tk()

# Función para abrir el formulario principal
def abrir_menu_algebra():
    menu_algebra = tk.Toplevel(root)
    
    # Botón "ER" en el formulario principal
    btn_er = tk.Button(menu_algebra, text="ER", command=abrir_form_er)
    btn_er.pack()

    # Botón "Historial" en el formulario principal
    btn_historial = tk.Button(menu_algebra, text="Historial", command=abrir_historial)
    btn_historial.pack()

# Botón "Álgebra" en la ventana principal
btn_algebra = tk.Button(root, text="Álgebra", command=abrir_menu_algebra)
btn_algebra.pack()

# Ejecutar la aplicación
root.mainloop()
