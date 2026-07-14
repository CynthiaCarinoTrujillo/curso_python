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

num_uno=5
num_dos=10
print(f"la suma de {num_uno} y {num_dos} es {num_uno + num_dos}")
#el valor de las variables num_uno y num_dos se convierte internamente en una cadena durante el proceso de interpolación.

#corte de cadenas y cómo funciona

#cada carácter en una cadena puede ser identificado por su índice (comenzando desde cero)
#y accedido usando la notación de corchetes

print("Accediendo a una letra dentro de una cadena" , lastname[4]) #imprime una letra de la cadena lastname

#El corte de cadenas te permite extraer una porción de una cadena o trabajar solo con una parte específica de ella. 
#sintaxis ---> string[start:stop]

print("Corte de cadenas" , lastname[5:8]) #imprime una porcion de la cadena lastname Gonzalez

"""Tener en cuenta que el índice stop no es inclusivo, 
por lo que [5:8] solo extrae los caracteres desde el índice 5 hasta 
sin incluir, el carácter del índice 8.

Tambien se puede omitir el indice start o stop y python asumira el valor por defecto"""

print("Omitiendo el indice start" , lastname[:6])
print("Omitiendo el indice stop", lastname[5:])

# cortar una cadena no modifica la cadena original
#puedes omitir los índices de start como de stop, lo que extraerá toda la cadena

print(lastname[:]) #imprime toda la cadena lastname

lista_edades=[i for i in range(0,10)]
#existe un parámetro opcional step, que se usa para especificar el incremento entre cada índice en el slice.
print("Usando el parámetro step", lastname[0:9:2]) #imprime los caracteres desde el índice 0 hasta el 9, con un incremento de 2
"""
sintaxis ---> string[start:stop:step] la division se realiza de la siguiente manera:
- start: índice inicial desde donde se comenzará a cortar la cadena.
- stop: índice final hasta donde se cortará la cadena (sin incluir el carácter en este indice)
- step: especifica el salto a dar mientras recorre la lista. 2 hace que imprimas de 2 en 2
"""
print(lista_edades[::2])    #imprime los elementos de la lista desde el índice 0 hasta el final, con un incremento de 2
print(lista_edades[::3])
print(lista_edades[::-1]) #si el numero es negativo recorre la lista desde el final, al reves

lista_edades_al_reves = lista_edades[::-1]
print(lista_edades_al_reves)