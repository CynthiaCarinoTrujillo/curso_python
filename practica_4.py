#concatenación de cadenas y la interpolación de cadenas
#En Python, puedes combinar múltiples cadenas juntas con el operador más (+). 
# Este proceso se llama concatenación de cadenas. EL + SOLO SIRVE EN STRING, no enteros.

name="Pedro"
lastname="Gonzalez"
print("Prueba de concatenacion " + name + " " + lastname)

#Python requiere que todos los elementos sean cadenas antes de poder concatenarlos.
#Puedes convertirlos a cadenas 
edad=32
datos_persona= name + " " + lastname + " " + str(edad) #convertimos edad a string para poder concatenarla

print(datos_persona)

"""
También puedes usar el operador de asignación aumentada para la concatenación. Este se 
representa con un más y un signo igual (+=), y realiza tanto la concatenación como la 
asignación en un solo paso. 
"""
peso=54.3
datos_persona+= " " + str(peso) #convertimos peso a string para poder concatenarla
print(datos_persona)

""" El proceso de insertar variables y expresiones en una cadena se llama interpolación de 
cadenas. Python tiene una categoría de cadena llamada f-strings 
(abreviatura de literales de cadena formateados)
Las cadenas f comienzan con f (ya sea en minúsculas o mayúsculas) antes de las comillas, 
y te permiten insertar variables o expresiones dentro de campos de reemplazo indicados
por llaves ({}).
"""
print(f"prueba de interpolacion: {name} {peso}")

variable_interpolada=f"yo soy {name}"
print(variable_interpolada)