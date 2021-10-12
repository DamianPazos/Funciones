'''
Realiza una función llamada area_rectangulo() 
que devuelva el área del rectángulo a partir de una base y una altura. 
Calcula el área de un rectángulo de 15 de base y 10 de altura
'''

# Inicio la funcion
def area_rectangulo(base,altura):
    return "El area de un rectangulo es {} metros cuadrados".format(base*altura) # Retorno el dato de la base

# Inicio funcion para convertir los datos a numeros
def convertir(dato):
	while dato.isnumeric() == False:
		print("¡Lo ingresado no es un número!")
		dato = input("Ingrese el dato nuevamente: ")
	dato = int(dato)
	return dato

# Ingreso el numero el cual va ir en la funcion
base_ingresada = input("Ingrese la base: \n")
base_ingresada = convertir(base_ingresada) # La convierto en int

# Ingreso el numero el cual va ir en la funcion
altura_ingresada = input("Ingrese la altura: \n")
altura_ingresada = convertir(altura_ingresada) # La convierto en int

print(area_rectangulo(base_ingresada,altura_ingresada)) # Aplico la funcion con los datos ingresados
print(area_rectangulo(15,10)) # Aplico la funcion con los datos pedidos en el ejercicio