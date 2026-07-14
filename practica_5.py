#métodos comunes de cadenas
"""
Un método es una función que pertenece a un objeto o clase específicos.
Los métodos deben ser llamados en el objeto al que pertenecen escribiendo 
el objeto seguido de un punto y la llamada al método. 
"""
variable_cadena="HoLa AmIgOs"
print(variable_cadena)

#upper(): Devuelve una nueva cadena con todos los caracteres convertidos a mayúsculas.
print(variable_cadena.upper())

#lower(): Devuelve una nueva cadena con todos los caracteres convertidos a minúsculas.
print(variable_cadena.lower())

#strip(): Devuelve una nueva cadena con los caracteres especificados de inicio y final eliminados.
#Si no se pasa ningún argumento, elimina los espacios en blanco de inicio y final.
cadena_con_espacios = " Las flores son amarillas "
cadena_inicio_fin = "r Afuera llueve r"
print(cadena_con_espacios.strip())
print(cadena_inicio_fin.strip("r"))

""" replace(caracteres1, caracteres2): Devuelve una nueva cadena con todas las ocurrencias de 
caracteres1 reemplazadas por caracteres2."""
despedida="Nos vemos el martes"
print(despedida.replace("Nos vemos", "Te veo")) #imprime te veo el martes

#entrada de usuario
nombre=input("Como te llamas ")
print("hola ", nombre)