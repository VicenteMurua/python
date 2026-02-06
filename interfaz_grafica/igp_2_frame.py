from tkinter import *

def configuracion_inicial_ventana(ventana: Tk):
    ventana.title('Primer Ventana Gráfica')
    #ventana.resizable(width=False, height=False)
    #ventana.geometry('600x400')
    ventana.config(bg="black")

def main ():
    raiz = Tk()
    configuracion_inicial_ventana(raiz)

    miframe = Frame()
    miframe.pack()
    miframe.config(bg="white")
    miframe.config(width='600', height='400')
    raiz.mainloop()

if __name__ == '__main__':
    main()