saludo = "hola"
letra = "h"
indice_de_letra = saludo.find(letra)

entrelazo_saludo_entre_mundo = saludo.join("mundo")
# Transformaciones y chequeos de strings
mayuscula = saludo.upper()
mayuscula.isupper()
minuscula = saludo.lower()
minuscula.islower()
titulo = saludo.title()
titulo.istitle()
# Transformaciones
## texto
inicio_mayuscula = saludo.capitalize()
intercambio = saludo.swapcase()
## strips
saludo.strip()
saludo.rstrip() # strip derecho
saludo.lstrip() # strip izquierdo
## split
saludo.rsplit() # comienza a dividir desde la derecha
saludo.split()
saludo.splitlines()
# Preguntas
es_alfanumerico = saludo.isalnum() # solo letra o numero no simbolos ni espacios
es_letra = saludo.isalpha() # mayususculas o minusculas
es_ascii = saludo.isascii() # falla con la ñ

# Numeros
es_solo_numero = saludo.isdigit() # Acepta dígitos decimales + superíndices/subíndices Unicode
saludo.isdecimal() # Solo acepta dígitos decimales “normales” (0–9)
saludo.isnumeric() # acepta lo mismo que isdecimal y numeros de otros sistemas
"""
Fracciones: ½, ⅓
Números romanos Unicode: Ⅻ
Números circled: ①
"""
# evitar errores
saludo.isidentifier() # chequea que el texto no sea palabra reservada
saludo.isprintable()
saludo.isspace()
