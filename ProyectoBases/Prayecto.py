import tkinter as tk
from tkinter import messagebox

def agregar():
    # abrir una pestaña para agregar un cliente
    ventana = tk.Toplevel()
    ventana.title("Agregar Cliente")
    ventana.geometry("400x350")
    ventana.resizable(0, 0)
    ventana.configure(background='green')

    btn_guardar = tk.Button(ventana, text="Guardar", command=guardar_cliente)
    btn_guardar.pack(pady=50)
    btn_guardar.pack(side="bottom", anchor="s")
    btn_guardar.config(width=20, height=2)

    # Aquí puedes poner los campos para agregar un cliente

    # Nombre
    lbl_nombre = tk.Label(ventana, text="Nombre")
    lbl_nombre.place(x=50,y=30)
    lbl_nombre.config(width=10, height=2)

    txt_nombre = tk.Entry(ventana)
    txt_nombre.place(x=200,y=30)

    # Apellido
    lbl_apellido = tk.Label(ventana, text="Apellido")
    lbl_apellido.place(x=50,y=80)
    lbl_apellido.config(width=10,height=2)

    txt_apellido = tk.Entry(ventana)
    txt_apellido.place(x=200,y=80)

    # Edad
    lbl_edad = tk.Label(ventana, text="Edad")
    lbl_edad.place(x=50,y=130)
    lbl_edad.config(width=10,height=2)

    txt_edad = tk.Entry(ventana)
    txt_edad.place(x=200,y=130)

    # Cedula
    lbl_cedula = tk.Label(ventana, text="Cedula")
    lbl_cedula.place(x=50,y=180)
    lbl_cedula.config(width=10,height=2)

    txt_cedula = tk.Entry(ventana)
    txt_cedula.place(x=200,y=180)


  
                        
def guardar_cliente():
    # Aquí puedes poner la lógica para guardar el cliente
    messagebox.showinfo("Guardar Cliente", "Funcionalidad de guardar cliente no implementada aún")

def agregaremp():
    
    ventana = tk.Toplevel()
    ventana.title("Agregar Empleado")
    ventana.geometry("400x400")
    ventana.resizable(0, 0)
    ventana.configure(background='green')

def ver_base_de_datos():
    # Aquí puedes poner la lógica para mostrar la base de datos
    messagebox.showinfo("Ver Base de Datos", "Funcionalidad de ver base de datos no implementada aún")

def inicio():
    messagebox.showinfo("Inicio", "Funcionalidad de inicio no implementada aún")

def salir():
    ventanaprincipal.quit()

# Crear la ventana principal
ventanaprincipal = tk.Tk()
ventanaprincipal.title("Empresa de Acarreos")
ventanaprincipal.configure(background='blue')
# la ventana se ajusta a la pantalla
ventanaprincipal.state("zoomed")



# Botones
btn_agregaremp = tk.Button(ventanaprincipal, text="Agregar Empleado", command=agregaremp)
btn_agregaremp.place(x=200,y=30)
btn_agregaremp.config(width=20, height=2)

btn_agregaremp = tk.Button(ventanaprincipal, text="Agregar Cliente", command=agregar)
btn_agregaremp.place(x=540, y=30)
btn_agregaremp.config(width=20, height=2)


btn_ver = tk.Button(ventanaprincipal, text="Ver Empleados", command=ver_base_de_datos)
btn_ver.place(x=370,y=30)
btn_ver.config(width=20, height=2)

btn_salir = tk.Button(ventanaprincipal, text="Salir", command=salir)
btn_salir .place(x=710,y=30)
btn_salir.config(width=20, height=2)

btn_inicio = tk.Button(ventanaprincipal, text="Inicio", command=inicio) 
btn_inicio.place(x=30, y=30)
btn_inicio.config(width=20, height=2)

imagen = tk.PhotoImage(file="acarreos.png")
lbl_imagen = tk.Label(ventanaprincipal, image=imagen)
imagen.config(width=700, height=400)
#agrandar imagen
lbl_imagen.image = imagen
#posicion de la imagen
lbl_imagen.place(x=50, y=100)


# Ejecutar el bucle principal de la interfaz
ventanaprincipal.mainloop()
