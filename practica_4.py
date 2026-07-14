#concatenación de cadenas y la interpolación de cadenas
#En Python, puedes combinar múltiples cadenas juntas con el operador más (+). 
# Este proceso se llama concatenación de cadenas. EL + SOLO SIRVE EN STRING, no enteros.

name="Pedro"
lastname="Gonzalez"
print("Prueba de concatenacion " + name + " " + lastname)

#Python requiere que todos los elementos sean cadenas antes de poder concatenarlos.
#Puedes convertirlos a cadenas 
edad=54
datos_persona= name + " " + lastname + " " + str(edad) #convertimos edad a string para poder concatenarla

print(datos_persona)
