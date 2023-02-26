from tkinter import *
class Maestro:
    def mostrarinterfazmaestro():   
        window=Tk()
        window.resizable(False,False)
        window.title("Alumno")
        window.geometry("500x300")
        window.config(bg="purple")

        panel=Frame()
        panel.pack()
        panel.config(width="500",height="500")
        panel.config(bg="green")

        nombre=Label(text="Nombre")
        nombre.pack()
        nombre.place(x=0,y=0)
        mainloop()