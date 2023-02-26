from tkinter import *
from Valumno import *
from Vmaestro import *
class Index():
    def mostrarindex():
        window=Tk()
        window.resizable(False,False)
        window.title("Menu")
        window.geometry("500x300")
        panel=Frame()
        panel.pack()
        panel.config(width="500",height="500")
        panel.config(bg="green")
        titulo=Label(text="Registro de datos")
        titulo.pack()
        titulo.place(x=200,y=500)
        def boton1():
            try:
                Alumno.mostrarinterfazalumno()
            except:
                print("error")
                
        def boton2():
            try:
                Maestro.mostrarinterfazmaestro()
            except:
                print("error")

        
        opcion1=Button(command=boton1,text="Alumno")
        
        opcion1.pack()
        opcion1.place(x=150,y=150)

        opcion2=Button(command=boton2,text="Maestro")
        opcion2.pack()
        opcion2.place(x=300,y=150)
        mainloop()

    mostrarindex()
