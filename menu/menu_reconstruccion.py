import time

while True:
    menu = actual()
    menu.mostrar()
    eleccion = input('->:')
    opcion = menu.opciones.get(eleccion)

    if opcion not in menu.opciones:
        print('Opcion no valida')
        for i in range(3):
            time.sleep(0.5)
            print('.')
        continue
    opcion()