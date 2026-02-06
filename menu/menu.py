from Data_Structures.fifo_lifo.stacks import Stack
from menu.menu_reconstruccion import eleccion
from menu.opciones import *
from menu.opciones import Opciones


def menu():
    menu1: Opciones = Opciones(dict_principal)
    menu2: Opciones = Opciones(dict_secundario)
    menu3: Opciones = Opciones(dict_final)
    menues: dict = {
        1: menu1,
        2: menu2,
        3: menu3,
    }
    menu: Stack = Stack()
    menu.push(menu1)
    while True:
        menu_actual: Opciones = menu.peek()
        menu_actual.mostrar()
        eleccion = input("Elige una opcion: ")
        if eleccion not in menu_actual.opciones:
            print("Opcion no valida")
            continue
        menu_actual.opciones[eleccion]
        menu.push(menues[eleccion])


def main():
    menu()

if __name__ == "__main__":
    main()