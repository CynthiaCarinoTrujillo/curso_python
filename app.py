
#PRACTICA 1 PYTHON (PRUEBA DE VARIABLES, TIPOS DE DATOS Y COLECCIONES)

"""
Entorno de Python en Windows. Instalar wsl2 es un Subsistema de Windows para Linux 2
- dentro de visual studio click en izquierda inferior para conectar WSL 
- Abrir el fichero a trabajar
"""

#Declaracion de las variables en Python
"""Los nombres de las variables son sensibles a mayúsculas
Los nombres de las variables empiezan con una letra o guion bajo, nunca con un numero
snake case es una convencion donde los nombres de las variables deben estar en 
minúsculas y palabras separadas por un guión bajo"""

#ejemplo de declaracion de variables
fruta_favorita="mango"

#IMPRESIONES
print(nombre)
print("la fruta favorita de", nombre, "es", fruta_favorita)
print('Hello', 'mundo')
print('Hello mundo!')

"""
Python es un lenguaje de tipado dinámico como JavaScript, es decir
NO es necesario declarar explícitamente LOS tipos para las variables. 
El lenguaje sabe qué tipo de dato es una variable basado en lo que le asignes"""

#Ejecucion de python
"""
Cuando un programa se ejecuta, Python procesa tu código línea por línea. 
Si llega a una línea donde se espera que un cierto objeto se comporte de una manera 
que no puede, Python se detendrá y mostrará un error. En Python, los errores de tipo 
pueden revelarse durante la ejecución, cuando el programa está realmente corriendo 
y usando tu código"""

#prueba de tipos de datos
numero_decimal=3.1416
print(numero_decimal)
valor_booleano= False
print(valor_booleano)

#COLECCIONES
#Conjunto, es una coleccion de datos UNICOS (no se pueden repetir) no ordenados, encerrados llaves
conjunto_no_ordenado={1,'Pablo', 3.12, False}
print(conjunto_no_ordenado, "Ha ordenado automaticamente") #impresion ordenada en automatico

#Diccionario es una coleccion de datos de pares clave-valor encerrados en llaves
diccionario_de_compra={"queso": "feta", "pan": "de semillas", "leche": "deslantosada", "costo": 100.50}
print(diccionario_de_compra)
print("Acceso al valor de la segunda clave", diccionario_de_compra["pan"]) #acceder a un valor del diccionario

#Tupla coleccion de datos ordenados e inmutables encerrados en parentesis, si se pueden repetir
tupla_animales=("perro","perro","gato") #parentesis
print("La tupla puede repetir valores",tupla_animales)

#Rango es una secuencia de números, usada en bucles, se utilizan parentesis
prueba_rango=range(1,10) #el rango empieza en 1 y termina en 9 se usan parentesis
print("El rango es una secuencia de numeros", prueba_rango) #imprime (1,10)
prueba_segundo_rango=range(6)
print("segunda prueba de rango", prueba_segundo_rango) #imprime (0,6)

#Lista es una colección de datos ordenados que admite varios tipos de datos, usa corchetes
prueba_lista=[1,"Juan", 23.5, True]
print("probando lista",prueba_lista)

#Ninguno, es un tipo de dato que representa la ausencia de valor, se puede usar para inicializar variables
ningun_valor=None
print(ningun_valor)