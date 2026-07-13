# funciones type() y isinstance()
#para ver el tipo de una variable se utiliza la funcion type()
#dentro del parentesis se pone la variable a evaluar

#declaracion de variable
color_favorito="blanco"

print("El tipo de variable es", type(color_favorito))

segunda_variable=53.12
print("Segunda variable es de tipo", type(segunda_variable))

tercera_variable=42
print("Tercera variable es de tipo", type(tercera_variable))

cuarta_variable={"cynthia", 31, 61.2} #set
print("Cuarta variable es de tipo", type(cuarta_variable))

quinta_variable={"nombre": "cynthia", "edad":"31"} 
print("quinta variable", type(quinta_variable)) #imprime diccionario

sexta_variable=("perro","gato","conejo") #tupla
print("sexta variable", type(sexta_variable))

septima_variable=range(78) #rango
print("septima variable", type(septima_variable))

octava_variable=["Casa", "coche", 43, 23.5, True] #lista
print("octava variable", type(octava_variable))

novena_variable=None
print("novena variable", type(novena_variable))

"""
La funcion isinstance() se utiliza para verificar si un objeto es una 
instancia de una clase en especifico. La función integrada isinstance() te 
permite comprobar si una variable coincide con un tipo de dato específico. 
Recibe un objeto y el tipo contra el que quieres verificarlo, y devuelve un booleano"""

anios_user="Hola"

#vamos a verificar si la variable anios_user es de tipo float
resultado=isinstance(anios_user,float)
print("resultado de la variable es", resultado)
#para ahorrarnos una variable podemos directamente imprimir el resultado
print("segunda verificacion", isinstance(anios_user, int))

#La función isinstance() también te permite verificar múltiples tipos a la vez.

resultado_multiple=isinstance(anios_user,(int, float)) #comprueba, es entero O decimal
print("resultado multiple", resultado_multiple) 

is_student = True
print(is_student, type(is_student)) #imprimes la variable y su tipo de dato