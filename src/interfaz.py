from tkinter import *

ventana =Tk()
ventana.title("Analizador C#")
ventana.geometry("1100x400")

def guardar_input():
    texto= cajaTexto1.get("1.0",END)
    print(texto)

etiqueta1= Label(ventana, text="Ingresa tu codigo aqui").place(relx=0.009, rely=0.05)
cajaTexto1 = Text(ventana,height=10, width=30).place(relx=0.005, rely=0.1, relwidth=0.5, relheight=0.7)
etiqueta2= Label(ventana, text="El resultado del analisis es...").place(relx=0.53, rely=0.05)
cajaTexto2 = Text(ventana,height=10, width=30).place(relx=0.52, rely=0.1, relwidth=0.474, relheight=0.7)
#e.grid(row =0, column = 0)

bLexico = Button(ventana, text= "Lexico",command =guardar_input).place(relx=0.005, rely=0.809, relwidth=0.1, relheight=0.1)
bSintactico = Button(ventana, text="Sintactico",command =guardar_input).place(relx=0.105, rely=0.809, relwidth=0.1, relheight=0.1)
bBorrar = Button(ventana, text="Limpiar",command =guardar_input).place(relx=0.205, rely=0.809, relwidth=0.1, relheight=0.1)
#bL.grid(row =0, column = 1)
#bS.grid(row =1, column = 1)


ventana.mainloop()

