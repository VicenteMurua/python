class Opciones:
    def __init__(self, opciones: dict[str, callable]):
        self.opciones: dict = opciones

    def mostrar(self):
        for opcion in self.opciones.keys():
            print(opcion)

dict_principal = {
    1: lambda: print("Opción 1 del Menú Principal"),
    2: lambda: print("Opción 2 del Menú Principal"),
    3: lambda: print("Opción 3 del Menú Principal"),
}

dict_secundario = {
    1: lambda: print("Opción 1 del Menú Secundario"),
    2: lambda: print("Opción 2 del Menú Secundario"),
    3: lambda: print("Opción 3 del Menú Secundario"),
}

dict_final = {
    1: lambda: print("Opción 1 del Menú Final"),
    2: lambda: print("Opción 2 del Menú Final"),
    3: lambda: print("Opción 3 del Menú Final"),
}