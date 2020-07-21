import lexico
import sintactico
from tkinter import *

ventana =Tk()
ventana.title("Analizador C#")
ventana.geometry("1100x400")

def input_Lexico():
    texto= cajaTexto1.get("1.0",END)
    out = lexico.analizar(texto)
    output(out)

def input_Sintactico():
    texto= cajaTexto1.get("1.0",END)
    out = sintactico.sintactico(texto)
    output(out)

def output(data):
    cajaTexto2.delete(1.0, END)
    for i in range(len(data)):
        line = data[i]
        cajaTexto2.insert(str(i+1) + ".0", str(line) + "\n")        

def borrar():
    cajaTexto1.delete(1.0, END)
    cajaTexto2.delete(1.0, END)

etiqueta1= Label(ventana, text="Ingresa tu codigo aqui").place(relx=0.009, rely=0.05)
cajaTexto1 = Text(ventana,height=10, width=30)
etiqueta2= Label(ventana, text="El resultado del analisis es...").place(relx=0.53, rely=0.05)
cajaTexto2 = Text(ventana,height=10, width=30)
#e.grid(row =0, column = 0)

bLexico = Button(ventana, text= "Lexico",command =input_Lexico).place(relx=0.005, rely=0.809, relwidth=0.1, relheight=0.1)
bSintactico = Button(ventana, text="Sintactico",command =input_Sintactico).place(relx=0.105, rely=0.809, relwidth=0.1, relheight=0.1)
bBorrar = Button(ventana, text="Limpiar",command =borrar).place(relx=0.205, rely=0.809, relwidth=0.1, relheight=0.1)
#bL.grid(row =0, column = 1)
#bS.grid(row =1, column = 1)
cajaTexto1.place(relx=0.005, rely=0.1, relwidth=0.5, relheight=0.7)
cajaTexto2.place(relx=0.52, rely=0.1, relwidth=0.474, relheight=0.7)

ventana.mainloop()

