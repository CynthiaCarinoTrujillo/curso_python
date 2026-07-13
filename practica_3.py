#cadenas y la inmutabilidad de las cadenas
"""
En algunos lenguajes de programación, los caracteres entre comillas 
simples se tratan de manera diferente que los rodeados por comillas dobles, 
pero en Python, se tratan igual"""

primer_cadena="Hola mundo"
#Puedes crear una cadena de múltiples líneas, usando comillas triples dobles o simples
segunda_cadena="""Carla es una excelente
programadora, ella es buena en python y java"""
tercera_cadena='''Carla 
lleva 
3 meses'''

#prueba de comillas simples y dobles
cuarta_cadena="Jose dijo: Hola" 
quinta_cadena='Juan tiene doble "comillas" en su frase'
print(cuarta_cadena)
print(quinta_cadena)
# la siguiente impresion, imprime comillas simples
print('hola \'comillas\' mundo') 
print("hola \"comilla doble\" mundo")

# Para obtener la longitud de una cadena, puedes usar la función incorporada len()
print("longitud de cadena", len(quinta_cadena))

"""Cada carácter en una cadena tiene una posición llamada índice. 
El índice es cero, lo que significa que el índice del primer carácter 
de una cadena es 0, el índice del segundo carácter es 1, y así sucesivamente. 
Para acceder a un carácter por su índice, usas corchetes ([]) con el índice del 
carácter que deseas acceder dentro"""

print("primer caracter de la cadena", cuarta_cadena[7])

"""La indexación negativa también está permitida, por lo que puedes obtener 
el último carácter de cualquier cadena con -1, el penúltimo carácter con -2, 
y así sucesivamente
"""
print("negativo", cuarta_cadena[-3])

"""En Python todos los datos se tratan como objetos, y algunos objetos son 
inmutables mientras que otros son mutables. 
Los tipos de datos inmutables no se pueden modificar o alterar una vez que se declaran. 
Puedes apuntar sus variables a algo nuevo, lo que se llama reasignación,
pero no puedes cambiar el objeto original en sí mismo agregando, eliminando o 
reemplazando cualquiera de sus elementos.

Las cadenas son tipos de datos inmutables en Python. Esto significa que puedes reasignar 
una cadena diferente a una variable
"""
probando_reasignacion="Hola mundo"
print(probando_reasignacion)
probando_reasignacion="Mangos"
print(probando_reasignacion)

#no se permite la modificación directa de una cadena
#mangos[0]='y' lo anterior no se puede hacer, ya que las cadenas son inmutables
