from tkinter import *
class Alumno:
    def mostrarinterfazalumno():
        window=Tk()
        window.resizable(False,False)
        window.title("Alumno")
        window.geometry("500x300")
        window.config(bg="red")

        panel=Frame()
        panel.pack()
        panel.config(width="500",height="500")
        panel.config(bg="green")

        nombre=Label(window,text="Nombre")
        nombre.pack()
        nombree=Entry(window)
        nombree.pack()
        
        boleta=Label(window,text="Boleta")
        boleta.pack()
        boletae=Entry(window)
        boletae.pack()

        grupo=Label(window,text="Grupo")
        grupo.pack()
        grupoe=Entry(window)
        grupoe.pack()

        correo=Label(window, text="Correo electrónico")
        correo.pack() 
        correoe=Entry(window)
        correoe.pack()
        
        def escribir():
            tnombre=nombree.get()
            print(tnombre)
            tboleta=boletae.get()
            print(tboleta)
            tgrupo=grupoe.get()
            print(tgrupo)
            tcorreo=correoe.get()
            print(tcorreo)
        enviar=Button(window,text="Submit",command=escribir)
        enviar.pack()
        

        mainloop()